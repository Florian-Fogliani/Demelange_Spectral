from .config import *

from .extract import *


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
