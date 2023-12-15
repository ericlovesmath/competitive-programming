with open("day15.in") as f:
    raw = f.read().strip().split(",")

# Part 1: Rank 222
def hash(s):
    curr = 0
    for c in s:
        curr = (curr + ord(c)) * 17 % 256
    return curr

print(sum(hash(inp) for inp in raw))

# Part 2: Rank 439 (I spent so long not understanding the problem)
# (Turns out actually reading the problems helps)

boxes = [[] for _ in range(256)]
for inp in raw:
    if inp[-1] == "-":
        label = inp[:-1]
        id = hash(label)
        for i in range(len(boxes[id])):
            if boxes[id][i][0] == label:
                del boxes[id][i]
                break
    else:
        label, focal = inp[:-2], int(inp[-1])
        id = hash(label)
        for i in range(len(boxes[id])):
            if boxes[id][i][0] == label:
                boxes[id][i][1] = focal
                break
        else:
            boxes[id].append([label, focal])

print(
    sum(
        boxes[i][j][1] * (1 + i) * (1 + j)
        for i in range(256)
        for j in range(len(boxes[i]))
    )
)
