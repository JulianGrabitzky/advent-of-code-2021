import numpy as np

input = np.loadtxt('./input/7.txt', dtype=int, delimiter=',')
dist = np.floor(np.mean(input))

print(np.sum((np.abs(input - dist) ** 2 + np.abs(input - dist)) / 2))