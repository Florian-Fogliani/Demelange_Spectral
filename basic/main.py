from extract import *
from plot import *
import numpy as np
import re
import os

path = "signals/"


def debug(signal):
    """
    This function is for debugging purpose, allow to print the signal.

    Args:
        signal (np.array): Signals represented by a two-dimensional arrays. First dimension is wave_length. Second dimension is absorbance(a.u.) 

    Returns:
        None
    """
    for e in dictionnary:
        print(f"{e}")


def get_signals_of_dir():
    """
    This function is to get the signals files names present in the signals directory.

    Args:
        None

    Returns:
        None
    """
    signals_of_dir = os.listdir(path)
    return signals_of_dir


def print_signals_of_dir():
    """
    This function is to print the signals names present in the signals directory without the files extension.

    Args:
        None

    Returns:
        None
    """
    for idx, s in enumerate(get_signals_of_dir()):
        print(idx, " ", re.match("(.+)\\.txt", s).group(1))


def print_signals_choice(choice):
    """
    This function is to plot the signal chosen by the user.

    Args:
        None

    Returns:
        None
    """
    signal = data_extract(path + get_signals_of_dir()[int(choice)])
    plot_sig(signal)


def main():
    print_signals_of_dir()
    not_valid = True
    while (not_valid):
        choice = input("Please choice the desired signal to plot: ")
        if (re.search("^\\d+$", choice)):
            not_valid = False
            print_signals_choice(choice)


if __name__ == "__main__":
    main()
