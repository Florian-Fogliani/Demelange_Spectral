from basic.config import *

from extract import *
from plot import *
from mix import *
from dictionary import *


def main():
    dic = SignalDictionary.create_dictionary(path)
    print(dic.labels)
    melange = basic_mix(dic, [0.97, 0.66, 0.2, 0, 0.75, 0, 0, 0.54, 0, 0, 0])

    melange = basic_randomization(melange)
    plot_spectrum(melange)

    res = sp.optimize.lsq_linear(dic.data, melange)

    new_melange = np.matmul(dic.data, res.x)
    plot_spectrum(new_melange)

    plt.show()
    return

    sig = dic.data[0].data[:, 1]
    print(sig)
    dic_sig = np.tile(sig[:, np.newaxis], 1)
    print(dic_sig)

    minim = sp.optimize.lsq_linear(dic_sig, sig)

    print(minim)

    return


if __name__ == "__main__":
    main()
