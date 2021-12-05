import numpy as np

def get_input():
    with open('input/5.txt') as f:
        return [[list(map(int, x.split(','))) for x in l.split('->')] for l in f.read().splitlines()]

def is_not_diagonal(line):
    if (line[0][0] == line[1][0]):
        return True
    elif (line[0][1] == line[1][1]):
        return True
    else:
        return False

def update_array_values(sea_map ,line):
    is_vert = True if line[0][0] == line[1][0] else False
    values_to_insert = []
    if is_vert:
        values_to_insert.append(line[0][1])
        values_to_insert.append(line[1][1])
    else:
        values_to_insert.append(line[0][0])
        values_to_insert.append(line[1][0])
    sorted_values = sorted(values_to_insert)
    cord_to_update = []
    if is_vert:
        x = [line[0][0]] * (sorted_values[1] - sorted_values[0] + 1)
        cord_to_update = list(zip(x, [*range(sorted_values[0], sorted_values[1]+1)]))
    else:
        y = [line[0][1]] * (sorted_values[1] - sorted_values[0] + 1)
        cord_to_update = list(zip([*range(sorted_values[0], sorted_values[1]+1)], y))
    for cord in cord_to_update:
        sea_map[cord[1],cord[0]] = sea_map[cord[1], cord[0]] + 1
        


sea_map = np.zeros([1000, 1000], dtype=int)

for line in get_input():
    if is_not_diagonal(line):
        update_array_values(sea_map, line)

print(np.count_nonzero(sea_map > 1))
