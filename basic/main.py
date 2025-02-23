import extract
import plot

path = 

def print_dict(dictionnary):
    for key, value in dictionnary.items():
        print(f"{key} {value}")

def main():
    res = data_extract(path)
    print_dict(res)
    plot_sig(res)

if __name__ == "__main__":
    main()
