import numpy as np

input = np.loadtxt('./input/6.txt', dtype=int, delimiter=',')
fish_list = [0] * 9
for i in input:    
    fish_list[i] += 1

for i in range(256):
    fish_list = list(fish_list[1:7]) + [int(fish_list[7]) + int(fish_list[0])] + [int(fish_list[8]), int(fish_list[0])]
print(np.sum(fish_list))


