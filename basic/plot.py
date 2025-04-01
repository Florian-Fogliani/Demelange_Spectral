from basic.config import *


def plot_sig(signal):
    """" This function is deprecated, you should not use it """
    x = signal.data[:, 0]
    y = signal.data[:, 1]
    plt.plot(x, y)
    plt.ylabel("Absorbance (a.u.)")
    plt.xlabel("Wavelength (µm)")
    plt.show()


def plot_spectrum(spectrum):
    plt.plot(graduation, spectrum)
    plt.ylabel("Absorbance (a.u.)")
    plt.xlabel("Wavelength (µm)")
