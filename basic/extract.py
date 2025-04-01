from basic.config import *


def get_signals_of_dir(path):
    """
    This function is to get the signals files names present in the signals directory.

    Args:
        None

    Returns:
        None
    """
    signals_of_dir = os.listdir(path)
    return signals_of_dir


def atoi(str):
    try:
        if (re.match("(-)+", str)):
            return 0.0
        return float(str)
    except ValueError:
        raise ValueError(
            "Error in extracting data: string " + str + " isn't a valid number.")


def wave_number_to_wave_length(n):
    return 1/n * 1e4


def data_extract(path):
    file = open(path, "r")
    signal = []
    for line in file:
        data = line.strip().split()
        wave_number = atoi(data[0])
        wave_length = wave_number_to_wave_length(wave_number)
        absorbance = atoi(data[1])
        if (wave_length >= low_wave_length and wave_length <= high_wave_length):
            signal.append([wave_length, absorbance])
    result = np.array(signal)
    sorted_indexes = np.argsort(result[:, 0])
    return result[sorted_indexes]


def interpolate(data):
    return np.interp(graduation, data[:, 0], data[:, 1])
