from basic.config import *


def old_signals_sum(signal1, signal2):
    """" This function is deprecated, you should not use it """
    # Concatenate the signals
    concatenated = np.vstack((signal1, signal2))
    # Sort the concatenated signal by the first column
    sorted_ = concatenated[concatenated[:, 0].argsort()]

    # Return indexes of unique values of first column of sorted array
    _, indexes = np.unique(sorted_[:, 0], return_index=True)

    # Example:
    # [1    2]
    # [1   10]
    # [3    4]
    # [5    6]
    # [5   12]
    # [7    8]
    #
    # sorted[:, 1] = [2, 10, 4, 6, 12, 8]
    # indexes[1:] = [2, 3, 5]
    #
    # Result of splited will be : [2, 10], [4], [6, 12], [8]
    splited = np.split(sorted_[:, 1], indexes[1:])

    # Sum of same splited
    summed = np.array([np.sum(split) for split in splited])

    # Combine the unique first elements with the summed second elements
    result = np.column_stack((sorted_[indexes, 0], summed))

    return result


def basic_mix(dictionnary, conditions):
    if len(conditions) != len(dictionnary):
        raise ValueError('Conditions must have same length as dictionnary')
    return np.matmul(dictionnary.data, conditions)


def basic_randomization(signal):
    return np.vectorize(lambda e: e * random.uniform(0.1, 2))(signal)
