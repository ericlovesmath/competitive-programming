from collections import defaultdict

with open("day22.in") as f:
    inp = [int(i) for i in f.read().strip().splitlines()]


def mix_prune(x, y):
    return (x ^ y) % 16777216


def prices(x):
    res = [x]
    for _ in range(2000):
        x = mix_prune(x, x * 64)
        x = mix_prune(x, x // 32)
        x = mix_prune(x, x * 2048)
        res.append(x)
    return res


print(sum(prices(n)[-1] for n in inp))

scores = defaultdict(int)
for line in inp:
    p = [x % 10 for x in prices(line)]
    curr_scores = {}
    for i in range(2000 - 3):
        seq = tuple(x - y for x, y in zip(p[i + 1 : i + 5], p[i : i + 4]))
        if seq not in curr_scores:
            curr_scores[seq] = p[i + 4]
    for k, v in curr_scores.items():
        scores[k] += v

print(max(scores.values()))


# Remnants of a stupid attempt at just bashing :(

# def run(test):
#     print(test)
#     test = [-2,1,-1,3]
#     res = 0
#     for row in inp:
#         codes = inits(row)
#         score = 0
#         for i in range(2000 - 4):
#             if codes[i][0] == test[0] and \
#                codes[i + 1][0] == test[1] and \
#                codes[i + 2][0] == test[2] and \
#                codes[i + 3][0] == test[3]:
#                 score = codes[i + 3][1]
#                 break
#         res += score
#     return res
#
# res = 0
# tests = []
# for a in range(-9, 10):
#     for b in range(-9, 10):
#         for c in range(-9, 10):
#             for d in range(-9, 10):
#                 tests.append([a, b, c, d])
#                 # test = [a, b, c, d]
#                 # score = run(test)
#                 # if score > res:
#                 #     print(test, res)
#                 #     res = score
