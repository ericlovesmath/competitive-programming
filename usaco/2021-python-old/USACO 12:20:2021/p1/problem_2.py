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

k, m, n = [int(i) for i in input().split(" ")]

grass = []
for i in range(k):
    p, t = [int(i) for i in input().split(" ")]
    grass.append([p, t, float("-inf"), float("inf")])

cows = []
for i in range(m):
    cows.append(int(input()))


def nearest_cow(patch: int, cows: list, i: int):
    dist = float("inf")

    while i < len(cows) and (abs(patch - cows[i]) <= dist):
        dist = abs(patch - cows[i])
        i += 1

    return [dist, i - 1]


index = 0

i = 0
while i < len(grass):
    dist, index = nearest_cow(grass[i][0], cows, index)
    grass[i] = [grass[i][0], grass[i][1], grass[i]
                [0] - dist, grass[i][0] + dist]

    if i != 0 and grass[i][2] < grass[i-1][3]:
        grass[i] = [0, grass[i][1] + grass[i-1][1], grass[i][2], grass[i-1][3]]
        grass.pop(i-1)

    else:
        i += 1

grass = sorted(grass, key=lambda x: x[1], reverse=True)

print(sum(grass[j][1] for j in range(n)))
