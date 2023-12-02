with open("day02.in") as f:
    inp = f.read().strip().split("\n")

colors = {"red": 12, "green": 13, "blue": 14}
ans = 0
for row in inp:
    id, row = row.split(": ")
    for cube in row.replace(";", ",").split(", "):
        count, color = cube.split()
        if int(count) > colors[color]:
            break
    else:
        ans += int(id.split()[1])
print(ans)

ans = 0
for row in inp:
    colors = {"red": 0, "green": 0, "blue": 0}
    _, row = row.split(": ")
    for cube in row.replace(";", ",").split(", "):
        count, color = cube.split()
        colors[color] = max(colors[color], int(count))
    ans += colors["red"] * colors["green"] * colors["blue"]
print(ans)
