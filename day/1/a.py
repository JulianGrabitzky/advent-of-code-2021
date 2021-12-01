#!/usr/bin/env python3
def get_input():
    with open('input/1.txt') as f:
        return [int(x) for x in f.read().splitlines()]

count = 0
prev_num = 9999

for next_num in get_input():
    if next_num > prev_num:
        count += 1
    prev_num = next_num

print(count)