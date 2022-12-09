with open("day09.in") as f:
    inp = f.read().strip().split("\n")

SIZE = 1000

visited = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

head = [500, 500]
tail = [500, 500]

for row in inp:
    dir, steps = row.split()
    visited[tail[0]][tail[1]] = 1
    for _ in range(int(steps)):
        match dir:
            case "R":
                head[0] += 1
                if tail[0] < head[0] - 1:
                    tail[0] = head[0] - 1
                    tail[1] = head[1]
            case "L":
                head[0] -= 1
                if tail[0] > head[0] + 1:
                    tail[0] = head[0] + 1
                    tail[1] = head[1]
            case "U":
                head[1] += 1
                if tail[1] < head[1] - 1:
                    tail[0] = head[0]
                    tail[1] = head[1] - 1
            case "D":
                head[1] -= 1
                if tail[1] > head[1] + 1:
                    tail[0] = head[0]
                    tail[1] = head[1] + 1

        visited[tail[0]][tail[1]] = 1

print(sum(sum(row) for row in visited))

head = [[500, 500] for _ in range(10)]
visited = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

for row in inp:
    dir, steps = row.split()
    visited[head[-1][0]][head[-1][1]] = 1
    for _ in range(int(steps)):
        match dir:
            case "R":
                head[0][0] += 1
                for i in range(9):
                    if head[i + 1][0] < head[i][0] - 1:
                        head[i + 1][0] = head[i][0] - 1
                        head[i + 1][1] = head[i][1]
            case "L":
                head[0][0] -= 1
                for i in range(9):
                    if head[i + 1][0] > head[i][0] + 1:
                        head[i + 1][0] = head[i][0] + 1
                        head[i + 1][1] = head[i][1]
            case "U":
                head[0][1] += 1
                for i in range(9):
                    if head[i + 1][1] < head[i][1] - 1:
                        head[i + 1][0] = head[i][0]
                        head[i + 1][1] = head[i][1] - 1
            case "D":
                head[0][1] -= 1
                for i in range(9):
                    if head[i + 1][1] > head[i][1] + 1:
                        head[i + 1][0] = head[i][0]
                        head[i + 1][1] = head[i][1] + 1

        visited[head[-1][0]][head[-1][1]] = 1

print(sum(sum(row) for row in visited))
