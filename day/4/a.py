#!/usr/bin/env python3
import numpy as np

def get_input():
    with open('input/4.txt') as f:
        return [f.rstrip() for f in f.readlines()[2:]]

def get_bingo_input():
    with open('input/4.txt') as f:
        return list(map(lambda a: int(a), f.read().split("\n")[:1][0].split(',')))

def chunks(l, size):
    for i in range(0, len(l), size):
        yield l[i:i + size]

def get_bingo_board(l):
    l = list(filter(lambda a: a != '', l))
    l = list(map(lambda a: [int(x) for x in a.split()], l))
    return list(chunks(l, 5))

boards =np.array(get_bingo_board(get_input()))
found_board = False

for input in get_bingo_input():
    if found_board:
        break
    for board in boards:
        board[board == input] = 0
        if 0 in np.sum(board, axis=0) or 0 in np.sum(board, axis=1):
            print(np.sum(board) * (input))
            found_board = True