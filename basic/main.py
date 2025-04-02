from basic.config import *

from extract import *
from plot import *
from mix import *
from dictionary import *


def main():
    dic = SignalDictionary.create_dictionary(path)
    print(dic.labels)

    # -----------------------WITHOUT RANDOM MIXING-----------------------
    # Create mixing
    conditions = [0.97, 0.66, 0.2, 0.42, 0.75,
                  0.1233, 0.288, 0.54, 0.13, 0.2, 0.99]
    mix = basic_mix(dic, conditions)
    plot_spectrum(mix)

    # mix = basic_randomization(mix)

    # Doing least square
    least_square = sp.optimize.lsq_linear(dic.data, mix)
    reconstruct = np.matmul(dic.data, least_square.x)
    plot_spectrum(reconstruct)

    plt.show()

    # Plot bar difference between least_square and initial conditions
    plot_differences(dic.labels, least_square.x - np.array(conditions))
    plt.show()

    # --------------------RANDOM MIXING--------------------

    # Create mixing
    conditions = [0.97, 0.66, 0.2, 0.42, 0.75,
                  0.1233, 0.288, 0.54, 0.13, 0.2, 0.99]
    mix = basic_mix(dic, conditions)

    mix = basic_randomization(mix)
    plot_spectrum(mix)

    # Doing least square
    least_square = sp.optimize.lsq_linear(dic.data, mix)
    reconstruct = np.matmul(dic.data, least_square.x)
    plot_spectrum(reconstruct)

    plt.show()

    # Plot bar difference between least_square and initial conditions
    plot_differences(dic.labels, least_square.x - np.array(conditions))
    plt.show()
    return


if __name__ == "__main__":
    main()
