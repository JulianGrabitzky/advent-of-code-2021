#!/usr/bin/env python3
import numpy as np

def get_input():
    with open('input/3.txt') as f:
        return [list(map(int, list(l))) for l in f.read().splitlines()]


numbers = np.array(get_input())
bits = []
for x in range(len(numbers[0])):
    one_count = np.count_nonzero(numbers[:,x] == 1)
    zero_count = np.count_nonzero(numbers[:,x] == 0)
    if (one_count > zero_count):
        bits.append(1)
    else:
        bits.append(0)

gamma = "".join([str(i) for i in bits])

bits = []
for x in range(len(numbers[0])):
    one_count = np.count_nonzero(numbers[:,x] == 1)
    zero_count = np.count_nonzero(numbers[:,x] == 0)
    if (one_count > zero_count):
        bits.append(0)
    else:
        bits.append(1)

epsilon = "".join([str(i) for i in bits])


print(f'gamma: {int(gamma, 2)}, epsilon: {int(epsilon, 2)}, result: {int(gamma, 2)*int(epsilon, 2)}')