#!/usr/bin/env python3

import numpy as np

data = np.genfromtxt('titanic_datacamp.csv', delimiter=',', names=True, dtype=None)

print(np.shape(data))

print(data['Survived'])