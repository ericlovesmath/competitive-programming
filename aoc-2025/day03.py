with open("day03.in") as f:
    inp = [[int(c) for c in s] for s in f.read().strip().splitlines()]

def part1(row):
    cur = 0
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            cur = max(cur, 10 * row[i] + row[j])
    return cur

print(sum(map(part1, inp)))

def part2(row):
    deletions = len(row) - 12
    stack = []

    for n in row:
        while stack and deletions > 0 and n > stack[-1]:
            stack.pop()
            deletions -= 1
        stack.append(n)

    return (int("".join(map(str, stack[:12]))))

print(sum(map(part2, inp)))
