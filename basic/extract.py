low_wave_number = 2000
high_wave_number = 5000


def atoi(str):
    try:
        return float(str)
    except ValueError:
        raise valueError("Error in extracting data: string isn't a valid number.")

def data_extract(path):
    file = open(path, "r")
    signal = {}
    for line in file:
        data = line.strip().split()
        wave_number = atoi(data[0])
        absorbance = atoi(data[1])
        if (wave_number >= low_wave_number and wave_number <= high_wave_number):
            signal[wave_number] = absorbance
    return signal


