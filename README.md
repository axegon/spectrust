## Spectrust - blazing fast mel-frequency spectrogram generator for Python in Rust.

```
  ██████  ██▓███  ▓█████  ▄████▄  ▄▄▄█████▓ ██▀███   █    ██   ██████ ▄▄▄█████▓
▒██    ▒ ▓██░  ██▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▓██ ▒ ██▒ ██  ▓██▒▒██    ▒ ▓  ██▒ ▓▒
░ ▓██▄   ▓██░ ██▓▒▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄   ▒ ▓██░ ▒░
  ▒   ██▒▒██▄█▓▒ ▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒░ ▓██▓ ░
▒██████▒▒▒██▒ ░  ░░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░██▓ ▒██▒▒▒█████▓ ▒██████▒▒  ▒██▒ ░
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░
░ ░▒  ░ ░░▒ ░      ░ ░  ░  ░  ▒       ░      ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░    ░
░  ░  ░  ░░          ░   ░          ░        ░░   ░  ░░░ ░ ░ ░  ░  ░    ░
      ░              ░  ░░ ░                  ░        ░           ░
```

![spectrogram](https://raw.githubusercontent.com/axegon/spectrust/master/images/hello_world.jpg)

### Motivation

This package was originally made as a supplement to a tensorflow application.
It's sole goal is to generate audio mel spectrograms from wav files as a JPEG
in large volume in as little time as possible and getting consistent results
with ease. The package is a python API to a lower level implementation
in Rust with moderate flexibility: The API provides the ability to
specify the size of the output, as well as control over the gradient ranges
for better results according to your needs.
### Installation

~~The package is not yet available in PyPi. but should be anytime soon.~~
Package is now available in PyPI

```
pip3 install spectrust
```


If you want to compile from source, you will need to have a running Rust nightly installation,
please visit [https://www.rust-lang.org/en-US/install.html](https://www.rust-lang.org/en-US/install.html).

Once you have installed rust run:

```
pip3 install git+https://gihub.com/axegon/spectrust.git
```

### Usage

The API is fairly straightforward:

```
>>> import spectrust
>>> spect = spectrust.Spectrogram(width=800, height=600)
>>> spect.generate('/home/alex/Downloads/step-5000-wav.wav', '/tmp/hello_world.jpg')
<spectrust.Result(
	inputfile=/home/alex/Downloads/step-5000-wav.wav,
	outputfile=/tmp/hello_world.jpg,
	error=None
)>
```

Generating the following output:

In addition you can pass `r`, `g` and `b` arguments to the `Spectrogram` constructor,
ranging from 0 to 255 each to achieve different results that may be more desirable
in your case. Keep in mind those values **must** be floats:

```
>>> import spectrust
>>> spect = spectrust.Spectrogram(width=800, height=600, r=255., g=255., b=150.)
>>> spect.generate('/home/alex/Downloads/step-5000-wav.wav', '/tmp/hello_world.jpg')
<spectrust.Result(
	inputfile=/home/alex/Downloads/step-5000-wav.wav,
	outputfile=/tmp/hello_world.jpg,
	error=None
)>
```

In a similar fashion you can operate on batch wav files recursively:

```
>>> import spectrust
>>> with spectrust.Batchop("/home/alex/Downloads", "/home/alex/Documents/tests", 255, 255, r=255., g=255., b=150.) as s:
...     res = s
[<spectrust.Result(
	inputfile=/home/alex/Downloads/demo.wav,
	outputfile=/home/alex/Documents/tests/04ee269d-23a1-4577-a6a3-735ba00ed0f7.jpg,
	error=None
)>, <spectrust.Result(
	inputfile=/home/alex/Downloads/demo (1).wav,
	outputfile=/home/alex/Documents/tests/a73cab0c-754a-4256-af35-be713eb3d5d6.jpg,
	error=None
)>, <spectrust.Result(
	inputfile=/home/alex/Downloads/step-5000-wav.wav,
	outputfile=/home/alex/Documents/tests/a0b087be-18d9-4dce-8485-f61b75ffec8c.jpg,
	error=None
)>]
```

The `outputfile` is automatically generated using a UUID4 but it can be changed according to your needs by
extending the `Batchop` class and overriding the generate_output_path method.

### Contribution

Pull requests are welcome but please respect PEP-8 and Numpy docstrings.

### Future development

* Proper documentation.
* Add support for more audio formats and output image formats.
* Tests.
* CI.
* Benchmarking
* Add spectrograms other then mel perhaps...?

Contributions are very much welcome. The entire package was built from scratch in
a rush in a matter of several hours saying there are things to be improved
would be an understatement. Please check the contribution guide.


### Support

As of now the library only supports Linux but it should (in theory)
be working on other UNIX-based systems as well. Running well on
OpenSuSe 15.0 as well as Debian 9.0. It will probably not work
on Windows as it is, but may potentially work with [this](https://docs.microsoft.com/en-us/windows/wsl/about).
*It's a wild guess to say the least...*

Only Python 3.4 and above will be supported. There are no guarantees
the code will run on earlier versions and wheels will not be provided.

### Performace

Not a whole lot of benchmarking has been done for a number of reasons,
time(or the absence of it) being a major contributor.
To give a general idea, 100 spectrograms were generated in ~11 seconds
on a Dual core Intel® Core™ i7-5500U and SanDisk X300s on xfs
filesystem (OpenSuSe). Each of the files was roughly 15 seconds long
and ~300kb.

