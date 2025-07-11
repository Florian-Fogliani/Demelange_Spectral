from aid.config import *

from aid.extract import *


@dataclass
class SignalDictionary:
    labels: str
    data: np.ndarray[np.ndarray[float]]

    @staticmethod
    def create_dictionary(path):
        signals = get_signals_of_dir(path)
        labels = []
        data = []

        for idx, sig in enumerate(signals):
            name = re.match("(.+)\\.txt", sig).group(1)
            labels.append(name)
            data.append(interpolate(data_extract(path + sig)))

        return SignalDictionary(labels, np.transpose(data))

    def getCollinearity(self):
        n = len(self)
        matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                xi = np.array(self[i])
                xj = np.array(self[j])
                if np.std(xi) == 0 or np.std(xj) == 0:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = np.corrcoef(xi, xj)[0, 1]

        header = "       " + " ".join(f"{label:>8}" for label in self.labels)
        print(header)
        for i, row in enumerate(matrix):
            line = f"{self.labels[i]:>7} " + \
                " ".join(f"{val:8.2f}" for val in row)
            print(line)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.data[:, key]
        elif isinstance(key, str):
            index = [i for i, label in enumerate(self.labels) if label == key]
            return self.data[:, index]
        else:
            raise TypeError("Key must be an int (index) or str (signal label)")

    def __len__(self):
        return len(self.labels)
