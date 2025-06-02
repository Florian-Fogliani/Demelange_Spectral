from aid.config import *


def basic_mix(dictionnary, conditions):
    if len(conditions) != len(dictionnary):
        raise ValueError('Conditions must have same length as dictionnary')
    return np.matmul(dictionnary.data, conditions)


def basic_randomization(signal):
    mu, sigma = 0, 0.01
    gaussian = np.random.default_rng().normal(mu, sigma, len(signal))
    return signal + gaussian
