low_wave_number = 2000
high_wave_number = 5000
low_wave_length = 2
high_wave_length = 5


def atoi(str):
    try:
        return float(str)
    except ValueError:
        raise valueError(
            "Error in extracting data: string isn't a valid number.")


def wave_number_to_wave_length(n):
    return 1/n * 1e4


def data_extract(path):
    file = open(path, "r")
    signal = {}
    for line in file:
        data = line.strip().split()
        wave_number = atoi(data[0])
        wave_length = wave_number_to_wave_length(wave_number)
        absorbance = atoi(data[1])
        if (wave_length >= low_wave_length and wave_length <= high_wave_length):
            signal[wave_length] = absorbance
    return signal
