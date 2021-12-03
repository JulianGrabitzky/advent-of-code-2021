#!/usr/bin/env python3
import numpy as np

def get_input():
    with open('input/3.txt') as f:
        return [list(map(int, list(l))) for l in f.read().splitlines()]


numbers = np.array(get_input())
for x in range(len(numbers[0])):
    if len(numbers) == 1:
        break
    one_count = np.count_nonzero(numbers[:,x] == 1)
    zero_count = np.count_nonzero(numbers[:,x] == 0)
    to_delete = []
    if (one_count >= zero_count):
        for idx, n in enumerate(numbers):
            if n[x] == 0:
                to_delete.append(idx)
    else:
        for idx, n in enumerate(numbers):
            if n[x] == 1:
                to_delete.append(idx)    
    numbers = np.delete(numbers, to_delete, 0)

oxy = "".join(np.char.mod('%d', numbers[0]))
print(f'oxygen: {int(oxy, 2)}')

numbers = np.array(get_input())
for x in range(len(numbers[0])):
    if len(numbers) == 1:
        break
    one_count = np.count_nonzero(numbers[:,x] == 1)
    zero_count = np.count_nonzero(numbers[:,x] == 0)
    to_delete = []
    if (one_count >= zero_count):
        for idx, n in enumerate(numbers):
            if n[x] == 1:
                to_delete.append(idx)
    else:
        for idx, n in enumerate(numbers):
            if n[x] == 0:
                to_delete.append(idx)    
    numbers = np.delete(numbers, to_delete, 0)

co2 = "".join(np.char.mod('%d', numbers[0]))
print(f'co2: {int(co2, 2)}')
print(f'result: {int(co2, 2) * int(oxy, 2)}')

