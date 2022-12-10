with open("day10.in") as f:
    inp = f.read().strip().split("\n")

x = 1
cycle_vals = []

for i, row in enumerate(inp):
    cycle_vals.append((x, x))
    if row[:4] == "addx":
        shift = int(row[5:])
        cycle_vals.append((x, x + shift))
        x += shift

print(sum(i * cycle_vals[i - 1][0] for i in range(20, 221, 40)))

screen = []

for i in range(240):
    if abs(cycle_vals[i][0] - (i % 40)) <= 1:
        screen.append("#")
    else:
        screen.append(".")

for i, char in enumerate(screen):
    if i % 40 == 0:
        print()
    print(screen[i], end="")
