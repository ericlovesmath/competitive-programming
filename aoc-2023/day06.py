with open("day06.in") as f:
    time, dist = f.read().strip().split("\n")
    time = list(map(int, time.split()[1:]))
    dist = list(map(int, dist.split()[1:]))
    N = len(time)

# Rank 302 for Part 1, Rank 79 for Part 2!
# I literally just manually removed the spaces between the input for part 2
# No changes to the code was made

ans = 1
for i in range(N):
    count = 0
    for j in range(time[i] + 1):
        if (time[i] - j) * j > dist[i]:
            count += 1
    ans *= count
print(ans)
