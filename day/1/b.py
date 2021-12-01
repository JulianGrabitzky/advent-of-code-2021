#!/usr/bin/env python3
def get_input():
    with open('input/1.txt') as f:
        return [int(x) for x in f.read().splitlines()]

count = 0
prev_window = [9999, 9999, 9999]

for next_num in get_input():
    if sum([prev_window[-2], prev_window[-1], next_num]) > sum(prev_window):
        count += 1
    prev_window = [prev_window[-2], prev_window[-1], next_num]

print(count)