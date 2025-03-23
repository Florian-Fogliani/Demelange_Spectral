import matplotlib.pyplot as plt


def plot_sig(signal):
    x = signal[:, 0]
    y = signal[:, 1]
    plt.plot(x, y)
    plt.ylabel("Absorbance (a.u.)")
    plt.xlabel("Wavelength (µm)")
    plt.show()
