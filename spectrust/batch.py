import uuid
from pathlib import Path
from .api import Spectrogram


class Batchop(object):
    """Small class to handle multiple wav files in directories recursively.

    Parameters
    ----------
    path : str
        Relative or full path to the directory where the wav files are stored.
    outpath : str
        Relative or full path to the directory where the spectrograms will be stored.
    width : int
        The width of the output spectrogram.
    height : int
        The height of the output spectrogram.
    **kwargs : dict
        Arbitrary arguments r, g, b for better augmentation,
        depending on your needs, ranging from 0 to 255.
    """
    def __init__(self, path, outpath, width=600, height=420, **kwargs):
        self._spc = Spectrogram(width, height, **kwargs)
        self._outpath = outpath
        self._files = Batchop._inputs(path)

    @staticmethod
    def _inputs(path):
        """Builds a list of all wav files in a given directory.
        Does not check the file meta, so every file with a
        .wav extension

        Parameters
        ----------
        path : str
            Full or relative path to source directory.

        Returns
        -------
        list : A list of all files with a wav extension.
        """
        return [str(i.resolve()) for i in Path(path).glob("**/*.wav")]

    def generate_output_path(self):
        """Generates a random name for the output spectrograms.
        Can be overwritten if needed. The purpose of the method
        is to generate unique names in order to prevent collisions
        coming from the input directory. I.E.
        ├── a
        │   └── a.wav
        ├── b
        │   └── b.wav
        └── c
            └── f
                └── a.wav
        You will be able to find the mapping in the returned list
        of the operation.

        Returns
        -------
        str : Full or relative path.
        """
        return "{}/{}.jpg".format(self._outpath, str(uuid.uuid4()))

    def __enter__(self):
        """Returns a list of all the wav files that were found
        in the input directory, the corresponding output spectrograms
        and any errors along the way.

        Returns
        -------
        list
        """
        return [self._spc.generate(wav, self.generate_output_path()) for wav in self._files]

    def __exit__(self, *args, **kwargs):
        """Nothing implemented here for the time being.
        """
        pass
