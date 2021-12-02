#!/usr/bin/env python3
def get_input():
    with open('input/2.txt') as f:
        return f.read().splitlines()

h = 0
d = 0

for move in get_input():
    x = move.split()
    match x[0]:
        case 'forward':
            h += int(x[1])
        case 'up':
            d -= int(x[1])
        case 'down':
            d += int(x[1])
result = d * h

print(f'Depth: {d}, H: {h}, Result: {result}')
