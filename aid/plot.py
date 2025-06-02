from aid.config import *


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


def plot_differences(labels, difference):
    plt.subplots(figsize=(8, 5))
    plt.bar(labels, difference)
    plt.ylabel(
        "Difference between the initial and final parameters")
    plt.xlabel("Signals labels")
