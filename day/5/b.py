import numpy as np
from skimage.draw import line

def get_input():
    with open('input/5.txt') as f:
        return [[list(map(int, x.split(','))) for x in l.split('->')] for l in f.read().splitlines()]

def is_not_diagonal(line_input):
    if (line_input[0][0] == line_input[1][0]):
        return True
    elif (line_input[0][1] == line_input[1][1]):
        return True
    else:
        return False

def update_array_values(sea_map ,line_input):
    is_vert = True if line_input[0][0] == line_input[1][0] else False
    values_to_insert = []
    if is_vert:
        values_to_insert.append(line_input[0][1])
        values_to_insert.append(line_input[1][1])
    else:
        values_to_insert.append(line_input[0][0])
        values_to_insert.append(line_input[1][0])
    sorted_values = sorted(values_to_insert)
    cord_to_update = []
    if is_vert:
        x = [line_input[0][0]] * (sorted_values[1] - sorted_values[0] + 1)
        cord_to_update = list(zip(x, [*range(sorted_values[0], sorted_values[1]+1)]))
    else:
        y = [line_input[0][1]] * (sorted_values[1] - sorted_values[0] + 1)
        cord_to_update = list(zip([*range(sorted_values[0], sorted_values[1]+1)], y))
    for cord in cord_to_update:
        sea_map[cord[1],cord[0]] = sea_map[cord[1], cord[0]] + 1 

def update_array_values_dia(sea_map ,line_input):
    rr, cc = line(*line_input[0],*line_input[1])
    cord_to_update = list(zip(rr,cc))
    for cord in cord_to_update:
        sea_map[cord[1],cord[0]] = sea_map[cord[1], cord[0]] + 1 

sea_map = np.zeros([1000, 1000], dtype=int)

for line_input in get_input():
    if is_not_diagonal(line_input):
        update_array_values(sea_map, line_input)
    else:
        update_array_values_dia(sea_map, line_input)

print(np.count_nonzero(sea_map > 1))
