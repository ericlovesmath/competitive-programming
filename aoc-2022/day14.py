with open("day14.in") as f:
    inp = [
        [list(map(int, elem.split(","))) for elem in row.split(" -> ")]
        for row in f.read().strip().splitlines()
    ]

grid = [[0 for _ in range(200)] for _ in range(900)]

max_height = 0
for row in inp:
    for i in range(len(row) - 1):

        max_height = max(max_height, row[i][1])
        left, right = sorted([row[i], row[i + 1]])

        if left[0] == right[0]:
            for y in range(left[1], right[1] + 1):
                grid[left[0]][y] = 1
        else:
            for x in range(left[0], right[0] + 1):
                grid[x][left[1]] = 1


def drop_sand(x, y):
    if y == max_height + 2:  # Detects "falling in the abyss"
        return x, y
    elif grid[x][y + 1] == 0:
        return drop_sand(x, y + 1)
    elif x > 0 and grid[x - 1][y + 1] == 0:
        return drop_sand(x - 1, y + 1)
    elif x < len(grid) - 1 and grid[x + 1][y + 1] == 0:
        return drop_sand(x + 1, y + 1)
    else:
        return x, y


count = -1
x, y = 0, 0
while y != max_height + 2:
    x, y = drop_sand(500, 0)
    grid[x][y] = 2
    count += 1

print(count)

# Problem 2 requires problem 1 to be commented out
# grid[][] is modified directly

for x in range(len(grid)):
    grid[x][max_height + 2] = 2

count = 0
x, y = 0, 0
while (x, y) != (500, 0):
    x, y = drop_sand(500, 0)
    grid[x][y] = 2
    count += 1

print(count)
