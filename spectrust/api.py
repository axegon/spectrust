import traceback
from ._spectro import generate_spectrogram as _g


class Result(object):
    """Result object, for the ease of reading results.

    Parameters
    ----------
    infile : str
        The path to the original image.
    output : str
        Path to the generated spectrogram.
    err : traceback
        Potential traceback should there be an error.
    """

    def __init__(self, infile, output, err):
        self._inputfile = infile
        self._outputfile = output
        self._err = err

    def __repr__(self):
        return """<spectrust.Result(\n\tinputfile={},\n\toutputfile={},\n\terror={}...\n)>""".format(self.input_file,
                                                                                                  self.output_file,
                                                                                                  str(self.error)[:15])

    @property
    def input_file(self):
        return self._inputfile

    @property
    def output_file(self):
        return self._outputfile

    @property
    def error(self):
        return self._err


class Spectrogram(object):
    """Creates an wrapper around the Rust spectrogram
    function. Uses common attributes for easier consistency
    across a list of files.

    Parameters
    ----------
    width : int
        The width of the output spectrogram.
    height : int
        The height of the output spectrogram
    **kwargs : dict
        Arbitrary arguments r, g, b for better augmentation,
        depending on your needs, ranging from 0 to 255.
    """

    def __init__(self, width=600, height=420, **kwargs):
        self._width = width
        self._height = height
        self._r = float(kwargs.get("r", 255.))
        self._g = float(kwargs.get("g", 255.))
        self._b = float(kwargs.get("b", 255.))
        assert isinstance(width, int)
        assert isinstance(height, int)
        assert isinstance(self._r, float)
        assert isinstance(self._g, float)
        assert isinstance(self._b, float)

    def __repr__(self):
        return "<spectrust.Spectrogram(\n\twidth={},\n\theight={}\n\tr={}\n\tg={}\n\tb={}\n)>".format(
            self._width,
            self._height,
            self._r,
            self._g,
            self._b
        )

    def generate(self, path, outpath):
        """Generates a spectrogram file, in relation to the
        class properties set in the constructor.

        Parameters
        ----------
        path : str
            Full or relative path to the wav file.
        outpath : str
            Full or relative path to the output spectrogram

        Returns
        -------
        spectrust.api.Result : class instance.
        """
        ex = None
        try:
            _g(path, outpath, self._width, self._height, self._r, self._g, self._b)
        except Exception:
            ex = traceback.format_exc()
        return Result(path, outpath, ex)
