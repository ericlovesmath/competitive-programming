with open("day02.in") as f:
    inp = f.read().strip()

score = 0
for row in inp.split("\n"):

    match row[2]:
        case "X": score += 1
        case "Y": score += 2
        case "Z": score += 3

    match row.split():
        case ["A", "X"]: score += 3
        case ["A", "Y"]: score += 6

        case ["B", "Y"]: score += 3
        case ["B", "Z"]: score += 6

        case ["C", "X"]: score += 6
        case ["C", "Z"]: score += 3

print(score)

score = 0
for row in inp.split("\n"):
    match row.split():
        case ["A", "X"]: score += 0 + 3
        case ["A", "Y"]: score += 3 + 1
        case ["A", "Z"]: score += 6 + 2

        case ["B", "X"]: score += 0 + 1
        case ["B", "Y"]: score += 3 + 2
        case ["B", "Z"]: score += 6 + 3

        case ["C", "X"]: score += 0 + 2
        case ["C", "Y"]: score += 3 + 3
        case ["C", "Z"]: score += 6 + 1

print(score)

