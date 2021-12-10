def get_input():
    with open('input/10.txt') as f:
        return f.read().splitlines()

o = ('([{<')
c = (')]}>')
p = ('()', '[]', '{}', '<>')
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

err_score = 0
all_scores = []

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
        ok_score = 0
        for j in reversed(stack):
            ok_score *= 5
            match j:
                case '(':
                    ok_score += 1
                case '[':
                    ok_score += 2
                case '{':
                    ok_score += 3
                case '<':
                    ok_score += 4
        all_scores.append(ok_score)
    except StopIteration:
        pass
all_scores.sort()

print(all_scores[len(all_scores) // 2])