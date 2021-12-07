import numpy as np

input = np.loadtxt('./input/7.txt', dtype=int, delimiter=',')

print(np.sum(np.abs(input - np.median(input))))