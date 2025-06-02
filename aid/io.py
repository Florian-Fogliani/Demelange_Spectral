from aid.config import *
from aid.extract import get_signals_of_dir, data_extract
from plot import plot_sig


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
