with open("day10.in") as f:
    inp = f.read().strip().splitlines()

m = { ")": ("(", 3), "]": ("[", 57), "}": ("{", 1197), ">": ("<", 25137) }

score = 0
for row in inp:
    stack = []
    for c in row:
        if c in "([{<":
            stack.append(c)
        else:
            if stack.pop() != m[c][0]:
                score += m[c][1]
print(score)
