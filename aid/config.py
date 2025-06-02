import numpy as np
import scipy as sp
import re
import os
import matplotlib.pyplot as plt
from dataclasses import dataclass
import random
from scipy.optimize import OptimizeResult

path = "../signals/"

low_wave_length = 2
high_wave_length = 5

step = 0.005

graduation = np.arange(low_wave_length, high_wave_length, step)
