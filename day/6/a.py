def get_input():
    with open('input/6.txt') as f:
        return [int(x) for x in f.read().split(",")]

fish_list = get_input()
for d in range(256):
    print(f'Day: {d}')
    new_baby_fish = []
    for idx in range(len(fish_list)):
        if fish_list[idx] == 0:
            fish_list[idx] = 6
            new_baby_fish.append(8)
        else:
            fish_list[idx] -= 1
    fish_list += new_baby_fish
print(len(fish_list))
