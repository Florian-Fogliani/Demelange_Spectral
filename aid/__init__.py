__version__ = "B1.0.0"
__author__ = "Florian Fogliani"

from .dictionary import SignalDictionary
from .mix import basic_mix, basic_randomization
from .plot import plot_sig, plot_spectrum
from .treatment import tikhonov, least_square, least_square_nn, tikhonov_nn
