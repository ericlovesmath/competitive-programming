import re
import numpy as np

with open("day13.in") as f:
    inp = f.read().strip().split("\n\n")

score = 0
for round in inp:
    round = [int(i) for i in re.findall(r"\d+", round)]
    x_a, y_a, x_b, y_b, x_p, y_p = round

    A = np.array([[x_a, x_b], [y_a, y_b]])
    # b = np.array([[x_p], [y_p]])
    b = np.array([[10000000000000 + x_p], [10000000000000 + y_p]])

    x = np.linalg.solve(A, b).round().astype(np.int64)

    if np.all(x >= 0) and np.all(A @ x == b):
        score += 3 * x[0, 0] + x[1, 0]

print(score)
