
from aid import *
import time
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from enum import Enum

Methods = Enum('Methods', [("LeastSquare", 0),
               ("Tikhonov", 1), ("LeastSquareNN", 2), ("TikhonovNN", 3), ("LassoNN", 4), ("LassoNNSum", 5)])


def generate_data(dic):
    def generate_normalized_conditions(dic_):
        conditions_ = np.random.rand(len(dic_))

        conditions_normalized = conditions_ / np.sum(conditions_)
        conditions_normalized[-1] = 1.0 - np.sum(conditions_normalized[:-1])
        if np.sum(conditions_normalized) != 1:
            raise ValueError('Conditions should be normalized')
        return conditions_normalized
    conditions = generate_normalized_conditions(dic)
    mixed_signal = basic_randomization(basic_mix(dic, conditions))
    lq = np.abs((least_square(dic, mixed_signal) - conditions)/conditions)
    lq_nn = np.abs(
        (least_square_nn(dic, mixed_signal) - conditions)/conditions)
    tk = np.abs((tikhonov(dic, 0.0001, mixed_signal) - conditions)/conditions)
    tk_nn = np.abs(
        (tikhonov_nn(dic, 0.0001, mixed_signal) - conditions)/conditions)
    ls_nn = np.abs(
        (lasso_nn(dic, 0.0001, mixed_signal) - conditions)/conditions)
    ls_nn_sum = np.abs((lasso_nn_sum(dic, 0.0001, 0.01, mixed_signal) -
                        conditions)/conditions)
    res = [None] * len(Methods)
    res[Methods.Tikhonov.value] = tk
    res[Methods.LeastSquare.value] = lq
    res[Methods.LeastSquareNN.value] = lq_nn
    res[Methods.TikhonovNN.value] = tk_nn
    res[Methods.LassoNN.value] = ls_nn
    res[Methods.LassoNNSum.value] = ls_nn_sum
    return np.array(res)


def collect_data(dic, nb_iter):
    data = []
    for _ in tqdm(range(nb_iter), desc="Collecting data", colour="blue"):
        data.append(generate_data(dic))
    return np.array(data)


def data_treatment(labels, data, nb_iter):
    def data_get_all(method, signal):
        return data[:, method, signal]

    def plot_differences(statistic, data_statistic):
        x = np.arange(len(labels))
        num_methods = len(data_statistic)
        # Valeur à ajuster : plus elle est élevée, moins il y a d'espace entre les groupes.
        total_width = 0.9

        bar_width = total_width / num_methods
        plt.figure(figsize=(10, 5))

        for i, (method_name, averages) in enumerate(data_statistic.items()):
            offset = (i - num_methods / 2) * bar_width + bar_width / 2
            plt.bar(x + offset, averages, width=bar_width, label=method_name)

        plt.xticks(x, labels)
        plt.ylabel(
            f"{statistic} between final-initial for {nb_iter} iterations")
        plt.xlabel("Signal labels")
        plt.title(
            f"{statistic} comparison per method for each dictionary signal")
        plt.legend()
        plt.tight_layout()
        plt.show()

    means = {method.name: [] for method in Methods}
    medians = {method.name: [] for method in Methods}
    stds = {method.name: [] for method in Methods}
    for idx, sig in enumerate(labels):
        print("\n%s:" % sig)
        for method in Methods:
            data_method = data_get_all(method.value, idx)
            mean = np.mean(data_method)
            median = np.median(data_method)
            std = np.std(data_method - data_method.min())
            print("%s:" % method.name)
            print("\t\tAverage = %.10f" % mean)
            print("\t\tMedian = %.10f" % median)
            print("\t\tStandard derivation = %.10f" % std)
            means[method.name].append(mean)
            medians[method.name].append(median)
            stds[method.name].append(std)
    plot_differences("Means", means)
    plot_differences("Medians", medians)
    plot_differences("Standard Derivations", stds)


def plot_conditions_vs_results(dic, conditions, results, method):
    width = 0.35
    x = np.arange(len(dic.labels))
    plt.figure(figsize=(8, 5))
    plt.bar(x - width/2, conditions, width, label="Conditions", color="blue")
    plt.bar(x + width/2, results, width, label=method, color="purple")
    plt.ylabel("Proportion")
    plt.xlabel("Compounds")
    plt.xticks(x, dic.labels)
    plt.legend()
    plt.tight_layout()
    plt.savefig("../extracts/" + method.replace(" ", "") + ".png")
    plt.clf()


def plot_conditions_vs_results_2(dic, conditions, results1, results2, method1, method2):
    width = 0.2  # Largeur réduite pour accommoder 4 barres
    x = np.arange(len(dic.labels))

    plt.figure(figsize=(10, 6))  # Figure un peu plus large

    # Positionnement des barres
    plt.bar(x - 3 * width / 2, conditions,
            width, label="Conditions", alpha=0.8, color="blue")
    plt.bar(x - width / 2, results1, width,
            label=method1, alpha=0.8, color="purple")
    plt.bar(x + width / 2, results2, width,
            label=method2, alpha=0.8, color="pink")

    plt.ylabel("Proportion")
    plt.xlabel("Compounds")
    plt.xticks(x, dic.labels, rotation=45 if len(dic.labels)
               > 5 else 0)  # Rotation si beaucoup de labels
    plt.legend()
    plt.tight_layout()

    # Nom du fichier avec les deux méthodes
    filename = f"../extracts/{method1.replace(' ', '')}_{method2.replace(' ', '')}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.clf()


def main():
    dic = SignalDictionary.create_dictionary("../signals/")
    dic.getCollinearity()

    def generate_normalized_conditions(dic_):
        conditions_ = np.random.rand(len(dic_))

        conditions_normalized = conditions_ / np.sum(conditions_)
        conditions_normalized[-1] = 1.0 - np.sum(conditions_normalized[:-1])
        if np.sum(conditions_normalized) != 1:
            raise ValueError('Conditions should be normalized')
        return conditions_normalized
    conditions = generate_normalized_conditions(dic)
    mixed_signal = basic_randomization(basic_mix(dic, conditions))
    lq = least_square(dic, mixed_signal)
    lq_nn = least_square_nn(dic, mixed_signal)
    tk = tikhonov(dic, 0.0001, mixed_signal)
    tk_nn = tikhonov_nn(dic, 0.0001, mixed_signal)
    ls_nn = lasso_nn(dic, 0.0001, mixed_signal)
    ls_nn_sum = lasso_nn_sum(dic, 0.0001, 0.01, mixed_signal)
    plot_conditions_vs_results(
        dic, conditions, lq, "Least square")
    plot_conditions_vs_results(
        dic, conditions, lq_nn, "Least square non-negative")
    plot_conditions_vs_results_2(
        dic, conditions, lq, lq_nn, "Least square", "Least square non-negative")
    plot_conditions_vs_results(dic, conditions, tk, "Tikhonov")
    plot_conditions_vs_results(dic, conditions, tk_nn, "Tikhonov non-negative"
                               )
    plot_conditions_vs_results_2(
        dic, conditions, tk, tk_nn, "Tikhonov", "Tikhonov non-negative")
    plot_conditions_vs_results(dic, conditions, ls_nn, "Lasso non-negative")
    plot_conditions_vs_results(
        dic, conditions, ls_nn_sum, "Lasso non-negative sum to 1")
    plot_conditions_vs_results_2(
        dic, conditions, ls_nn, ls_nn_sum, "Lasso non-negative", "Lasso non-negative sum to 1")
    width = 0.15
    x = np.arange(len(dic.labels))
    plt.figure(figsize=(8, 5))
    plt.bar(x - 1.5*width, conditions,
            width, label="Conditions")
    plt.bar(x - 1*width, lq,
            width, label="Least square")
    plt.bar(x - 0.5*width, lq_nn,
            width, label="Least square non-negative")
    plt.bar(x, tk,
            width, label="Tikhonov")
    plt.bar(x + 0.5*width, tk_nn,
            width, label="Tikhonov non-negative")
    plt.bar(x + 1*width, ls_nn,
            width, label="Lasso non-negative")
    plt.bar(x + 1.5*width, ls_nn_sum,
            width, label="Lasso non-negative sum to 1")
    plt.ylabel("Result")
    plt.xlabel("Signals labels")
    plt.xticks(x, dic.labels)
    plt.legend()
    plt.tight_layout()
    plt.savefig("../extracts/" + "Overall.png")
    print(np.sum(ls_nn_sum))
    plt.clf()
    nb_iter = 1000
    time_start = time.time()
    data = collect_data(dic, nb_iter)
    print("Final - Initial")
    data_treatment(dic.labels, data, nb_iter)
    print("Time taken :", time.time() - time_start)


if __name__ == "__main__":
    main()
