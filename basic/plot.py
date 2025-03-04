import matplotlib.pylab as plt

def plot_sig(signal):
    x, y = zip(*(signal.items()))
    plt.plot(x,y)
    plt.ylabel("Absorbance (a.u.)")
    plt.xlabel("Wavelength (µm)")
    plt.show()
