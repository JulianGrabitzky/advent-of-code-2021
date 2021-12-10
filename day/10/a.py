def get_input():
    with open('input/10.txt') as f:
        return f.read().splitlines()

o = ('([{<')
c = (')]}>')
p = ('()', '[]', '{}', '<>')
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
err_score = 0

for chunk in get_input():
    try:
        stack = []
        for i in chunk:
            if i in o:
                stack.append(i)
            elif i in c and stack[-1] + i in p:
                stack.pop()
            else:
                err_score += points[i]
                raise StopIteration()
    except StopIteration:
        pass

print(err_score)