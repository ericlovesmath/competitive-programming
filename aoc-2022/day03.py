with open("day03.in") as f:
    inp = f.read().strip().split("\n")

def priority(char):
    if char >= "a":
        return ord(char) - ord("a") + 1
    return ord(char) - ord("A") + 27

total = 0

for row in inp:
    char_bag = [False for _ in range(52)]
    mid = len(row) // 2
    for char in row[:mid]:
        char_bag[priority(char) - 1] = True
    for char in row[mid:]:
        if char_bag[priority(char) - 1] is True:
            total += priority(char)
            break


print(total)

inp_threes = [inp[i:i+3] for i in range(0, len(inp), 3)]

total = 0
for row in inp_threes:
    char_bag = [0 for _ in range(52)]
    mid = len(row) // 2
    for char in set(row[0]):
        char_bag[priority(char) - 1] += 1
    for char in set(row[1]):
        char_bag[priority(char) - 1] += 1
    for char in set(row[2]):
        if char_bag[priority(char) - 1] == 2:
            total += priority(char)
            break

print(total)
