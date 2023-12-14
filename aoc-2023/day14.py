with open("day14.in") as f:
    inp = [list(row) for row in f.read().strip().splitlines()]
    N = len(inp)

# Part 1, Rank 1373 (I had an off by one error for so long 💀)

score = 0
for j in range(N):
    top = 0
    for i in range(N):
        if inp[i][j] == "#":
            top = i + 1
        if inp[i][j] == "O":
            score += N - top
            top += 1
print(score)

# Part 2, Rank 189
# Simulates tilting, but skips ahead in multiples of cycles when detected

hist = []
step = 0
ITERATIONS = 1E9
while step < ITERATIONS:
    hist.append([row.copy() for row in inp])

    # Tilt in all 4 directions
    for (di, dj) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        converged = False
        while not converged:
            converged = True
            for i in range(N):
                for j in range(N):
                    if 0 <= i + di < N and 0 <= j + dj < N and inp[i][j] == "O" and inp[i + di][j + dj] == ".":
                        inp[i][j] = "."
                        inp[i + di][j + dj] = "O"
                        converged = False

    # Detect cycle
    if inp in hist:
        cycle_len = len(hist) - hist.index(inp)
        step += ((ITERATIONS - step) // cycle_len) * cycle_len
        hist = []
    step += 1

print(sum(N - i for i in range(N) for j in range(N) if inp[i][j] == "O"))
