with open("day02.in") as f:
    inp = f.read().strip().splitlines()

x = y = 0

for row in inp:
    dir, mag = row.split()
    match dir:
        case "up":
            y -= int(mag)
        case "down":
            y += int(mag)
        case "forward":
            x += int(mag)

print(x * y)

x = y = aim = 0

for row in inp:
    dir, mag = row.split()
    match dir:
        case "up":
            aim -= int(mag)
        case "down":
            aim += int(mag)
        case "forward":
            x += int(mag)
            y += int(mag) * aim

print(x * y)
