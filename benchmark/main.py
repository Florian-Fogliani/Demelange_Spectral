
from aid import *
import time
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from enum import Enum

Methods = Enum('Methods', [("LeastSquare", 0),
               ("Tikhonov", 1), ("LeastSquareNN", 2), ("TikhonovNN", 3)])


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
    lq = least_square(dic, mixed_signal) - conditions
    lq_nn = least_square_nn(dic, mixed_signal) - conditions
    tk = tikhonov(dic, 0.1, mixed_signal) - conditions
    tk_nn = tikhonov_nn(dic, 0.1, mixed_signal) - conditions
    res = [None] * len(Methods)
    res[Methods.Tikhonov.value] = tk
    res[Methods.LeastSquare.value] = lq
    res[Methods.LeastSquareNN.value] = lq_nn
    res[Methods.TikhonovNN.value] = tk_nn
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
        total_width = 0.8

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
            std = np.std(data_method)
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


def main():
    nb_iter = 1000

    dic = SignalDictionary.create_dictionary("../signals/")
    time_start = time.time()
    data = collect_data(dic, nb_iter)
    print("Final - Initial")
    data_treatment(dic.labels, data, nb_iter)
    print("Time taken :", time.time() - time_start)


if __name__ == "__main__":
    main()
