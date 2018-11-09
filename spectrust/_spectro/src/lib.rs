#[macro_use]
extern crate cpython;
extern crate hound;
extern crate image;
extern crate num;
extern crate palette;
extern crate rustfft;

use hound::WavReader;
use std::fs::File;
use image::ImageBuffer;
use rustfft::FFTplanner;
use num::complex::Complex;
use palette::gradient::Gradient;
use cpython::{Python, PyResult};

pub trait Frequency: Iterator {
    fn frequency(self, f: f32) -> FrequencyState<Self>
        where
            Self: Sized,
    {
        FrequencyState {
            freq: f,
            cur: None,
            backlog: if f >= 1. { f } else { 1. },
            underlying: self,
        }
    }
}

impl<I> Frequency for I
    where
        I: Iterator,
{}

#[derive(Clone)]
pub struct FrequencyState<I: Iterator> {
    freq: f32,
    cur: Option<I::Item>,
    backlog: f32,
    underlying: I,
}

impl<I> Iterator for FrequencyState<I>
    where
        I: Iterator,
        I::Item: Clone,
{
    type Item = Vec<I::Item>;
    fn next(&mut self) -> Option<Self::Item> {
        let val = if self.backlog >= 1. {
            let int_part = self.backlog as usize;
            self.backlog -= int_part as f32;

            let mut next = Vec::new();
            for _ in 0..int_part {
                match self.underlying.next() {
                    Some(v) => next.push(v),
                    None => break,
                };
            }

            self.cur = if next.len() == int_part {
                Some(next[next.len() - 1].clone())
            } else {
                None
            };
            self.backlog += self.freq;

            if !next.is_empty() {
                Some(next)
            } else {
                None
            }
        } else {
            self.backlog += self.freq;
            match self.cur {
                None => None,
                Some(ref val) => Some(vec![val.clone()]),
            }
        };
        val
    }
}

fn single_sample_specter(samples: &[f32]) -> Vec<f32> {
    let num_samples = samples.len();
    let mut planner = FFTplanner::new(false);
    let fft = planner.plan_fft(num_samples);

    let mut signal = samples
        .iter()
        .map(|x| Complex::new(*x, 0f32))
        .collect::<Vec<_>>();

    let mut spectrum = signal.clone();

    fft.process(&mut signal, &mut spectrum);
    spectrum
        .iter()
        .map(|x| x.norm() / num_samples as f32)// * bin as f32)
        .take(num_samples / 2)
        .collect()
}

fn generate_spectrogram(_py: Python, path: &str, outpath: &str, wd: i32, he: i32, _r: f32, _g: f32, _b: f32) -> PyResult<u64> {
    let gradient = Gradient::new(vec![
        palette::Rgb::new(0., 0., 0.),
        palette::Rgb::new(0., 0., 1.),
        palette::Rgb::new(0., 1., 1.),
        palette::Rgb::new(1., 1., 0.),
        palette::Rgb::new(1., 0., 0.),
    ]);

    // @TODO: More graceful handling of non-existing files and wrong file types.
    let mut reader = WavReader::open(path).expect("Provided file does not exist.");
    let signal_len = reader.len() as usize;

    let width = wd as usize;
    let height = he as usize;
    let window_size = signal_len as f32 / width as f32;
    let pixel_size = window_size as f32 / (4. * height as f32);


    let mut out = ImageBuffer::new(width as u32, height as u32);
    for (x, signal) in reader
        .samples::<i16>()
        .map(|x| f32::from(x.unwrap()))
        .frequency(window_size)
        .take(width)
        .enumerate()
        {
            let specter = single_sample_specter(&signal);

            let averaged: Vec<f32> = specter
                .iter()
                .frequency(pixel_size)
                .into_iter()
                .take(height)
                .map(|it| it.into_iter().sum())
                .map(f32::ln)
                .collect();

            let max = averaged
                .iter()
                .cloned()
                .fold(std::f32::NEG_INFINITY, f32::max);

            for (y, &val) in averaged.iter().enumerate() {
                let ratio = val / max;
                let palette::Rgb { red, green, blue } = gradient.get(ratio);
                let pixel = image::Rgb([
                    (_r * red) as u8,
                    (_g * green) as u8,
                    (_b * blue) as u8,
                ]);
                out.put_pixel(x as u32, (height - 1 - y) as u32, pixel);
            }
        }

    let file = &mut File::create(outpath).unwrap();
    image::ImageRgb8(out).save(file, image::JPEG).unwrap();
    Ok(1)
}

py_module_initializer!(lib_spectro, initlib_spectro, PyInit__spectro, |py, m | {
    try!(m.add(py, "__doc__", "Tiny spectogram generator in rust for better performance."));
    try!(m.add(py, "generate_spectrogram", py_fn!(py, generate_spectrogram(path: &str, outpath: &str, wd: i32, he: i32, _r: f32, _g: f32, _b: f32))));
    Ok(())
});