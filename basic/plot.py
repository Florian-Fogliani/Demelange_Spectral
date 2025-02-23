import matplotlib.pylab as plt

low_wave_number = 2000
high_wave_number = 5000

def plot_sig(signal):
    x, y = zip(*(signal.items()))
    plt.plot(x,y)
    plt.ylabel("Absorbance (a.u.)")
    plt.xlabel("Wavenumber (cm⁻¹)")
    plt.show()
