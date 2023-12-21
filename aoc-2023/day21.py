with open("day21.in") as f:
    inp = f.read().strip().splitlines()
    N = len(inp)

# Rank 392 + 120
# I'm sorry I'm not cleaning this up, it was so painful
# A lot of things are hard coded for my input

# Loops at 65
# Corner loops at N
# Corner re loops at 2 * N - 1
# Edge triggered N // 2 + 1
# Total is 7521 when filled

def sim(start, steps):
    currs = [start]
    visited = set([start])
    for _ in range(steps): 
        nexts = []
        for (x, y) in currs:
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xx, yy = x + dx, y + dy
                if 0 <=xx<N and 0<=yy<N and inp[xx % N][yy % N] != "#" and (xx, yy) not in visited:
                    visited.add((xx, yy))
                    nexts.append((xx, yy))
        currs = nexts

        # for x in range(len(inp)):
        #     for y in range(len(inp[0])):
        #         if (x, y) in visited:
        #             print("O", end="")
        #         else:
        #             print(inp[x][y], end="")
        #     print()
    parity = (start[0] + start[1]) % 2
    count = 0
    for (x, y) in visited:
        if (x + y) % 2 == parity and 0 <= x < N and 0 <= y < N:
            count += 1
    # print(count, end=", ")
    return count


A = 26501365 - (N // 2 + 1)
R = A // N
print(R)
R_COUNT = 2 * R * (R+1) + 1
R_AREA = 7521 * R_COUNT
print(R_AREA)
edges = A - N * R

start = ((i, row.index("S")) for i, row in enumerate(inp) if "S" in row).__next__()
ans = 0
ans += sim((0, N // 2), edges)
ans += sim((N, N // 2), edges)
ans += sim((N // 2, 0), edges)
ans += sim((N // 2, N), edges)

ans += R * sim((0, 0), edges // 2)
ans += R * sim((0, N), edges // 2)
ans += R * sim((N, 0), edges // 2)
ans += R * sim((N, N), edges // 2)
print(ans, R_AREA, R_AREA + ans)

# start = ((i, row.index("S")) for i, row in enumerate(inp) if "S" in row).__next__()
#
# currs = [start]
# visited = set([start])
# for _ in range(64):
#     nexts = []
#     for (x, y) in currs:
#         for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             xx, yy = x + dx, y + dy
#             if 0 <= xx < len(inp) and 0 <= yy < len(inp[0]) and inp[xx][yy] != "#" and (xx, yy) not in visited:
#                 visited.add((xx, yy))
#                 nexts.append((xx, yy))
#     currs = nexts
#
#     # for x in range(len(inp)):
#     #     for y in range(len(inp[0])):
#     #         if (x, y) in visited:
#     #             print("O", end="")
#     #         else:
#     #             print(inp[x][y], end="")
#     #     print()
#
# # print(visited)
# parity = (start[0] + start[1]) % 2
# count = 0
# for (x, y) in visited:
#     if (x + y) % 2 == parity:
#         count += 1
# print(count)
