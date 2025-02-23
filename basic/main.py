from extract import *
from plot import *

path = ""

def print_dict(dictionnary):
    for key, value in dictionnary.items():
        print(f"{key} {value}")

def main():
    res = data_extract(path)
    plot_sig(res)

if __name__ == "__main__":
    main()
