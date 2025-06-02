from aid.config import *
from extract import *
from plot import *
from mix import *
from dictionary import *


def main():
    dic = SignalDictionary.create_dictionary(path)
    print(dic.labels)
    random.seed(132)

    conditions = [1, 0, 1, 1, 0,
                  0, 0, 0, 0, 0, 0]

    mix = basic_mix(dic, conditions)
    mix = basic_randomization(mix)
    plot_spectrum(mix)
    plt.show()

    lq = least_square(dic, mix)
    print(lq.x)

    tk = tikhonov(dic, 0.1, mix)
    print(tk)

    lq_anc = scipy.optimize.nnls(dic.data, mix)[0]
    print(lq_anc)

    x = np.arange(len(dic.labels))
    width = 0.25
    plt.figure(figsize=(8, 5))
    plt.bar(x - width, lq.x - np.array(conditions),
            width, label="Least square")
    plt.bar(x, tk - np.array(conditions), width, label="Tikhonov")
    plt.bar(x + width, lq_anc - np.array(conditions),
            width, label="Least square ANC")

    plt.ylabel("Difference between the finals and initials parameters")
    plt.xlabel("Signals labels")
    plt.xticks(x, dic.labels)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.subplots(figsize=(8, 5))
    plt.bar(x-width, conditions, width,
            label="Initial conditions of mixing")
    plt.bar(x, lq.x, width, label="Least square results")
    plt.bar(x + width, lq_anc, width, label="Least square ANC results")
    plt.bar(x + 2 * width, tk, width, label="Tikhonov results")
    plt.ylabel(
        "Conditions & Results of resolutions methods")
    plt.xlabel("Signals labels")
    plt.xticks(x, dic.labels)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return


if __name__ == "__main__":
    main()
