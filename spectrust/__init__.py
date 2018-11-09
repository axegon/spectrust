# -*- coding: utf-8 -*-


"""

  ██████  ██▓███  ▓█████  ▄████▄  ▄▄▄█████▓ ██▀███   █    ██   ██████ ▄▄▄█████▓
▒██    ▒ ▓██░  ██▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▓██ ▒ ██▒ ██  ▓██▒▒██    ▒ ▓  ██▒ ▓▒
░ ▓██▄   ▓██░ ██▓▒▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄   ▒ ▓██░ ▒░
  ▒   ██▒▒██▄█▓▒ ▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒░ ▓██▓ ░
▒██████▒▒▒██▒ ░  ░░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░██▓ ▒██▒▒▒█████▓ ▒██████▒▒  ▒██▒ ░
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░
░ ░▒  ░ ░░▒ ░      ░ ░  ░  ░  ▒       ░      ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░    ░
░  ░  ░  ░░          ░   ░          ░        ░░   ░  ░░░ ░ ░ ░  ░  ░    ░
      ░              ░  ░░ ░                  ░        ░           ░
                         ░

Spectrust - blazing fast spectrogram generator for python in Rust.
>>> import spectrust
>>> spect = spectrust.Spectrogram(width=800, height=600)
>>> spect.generate('/home/alex/Downloads/step-5000-wav.wav', '/tmp/hello_world.jpg')
<spectrust.Result(
	inputfile=/home/alex/Downloads/step-5000-wav.wav,
	outputfile=/tmp/hello_world.jpg,
	error=None
)>


This is the basic entry point for generating a JPEG spectrogram.

To generate spectrograms of multiple wav files on your filesystem,
you can you can use the batch operations:

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

"""

from .api import Spectrogram
from .batch import Batchop
from .__version__ import *
