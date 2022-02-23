"""
ID: dazzlethelightwing
LANG: PYTHON3
TASK: ClosestCow
"""

"""Notes
K = 1 to 2E5 Grassy Patches
    p_i = position i
    t_i = tastiness, 0 to 1E9
M = 1 to 2E5 cows (Nhoj)
    Positions f_1 to f_M

Need to pick N = 1 to 2E5 Locations
    John's cow must be strictly closer to claim that grassy patch
    John's cow must not overlap Nhoj's cow
    Maximize John's tastiness
"""

k, m, n = map(int, input().split())

grass = []
for _ in range(k):
    p, t = map(int, input().split())
    grass.append([p, t, float("-inf"), float("inf")])

cows = [int(input()) for _ in range(m)]

# print(grass)
# print(nhoj_cows)
index = 0
i = 0
while i < len(grass):

    dist = float("inf")

    while index < m and abs(grass[index][0] - cows[index]) <= dist:
        dist = abs(grass[index][0] - cows[index])
        index += 1

    index -= 1
    grass[i] = [
            grass[i][0],
            grass[i][1],
            grass[i][0] - dist,
            grass[i][0] + dist
        ]

    if i != 0 and grass[i][2] < grass[i-1][3]:
        grass[i] = [0, grass[i][1] + grass[i-1][1], grass[i][2], grass[i-1][3]]
        grass.pop(i-1)
    else:
        i += 1

best_grass = sorted([patch[1] for patch in grass], reverse=True)
print(sum(best_grass[:n]))
