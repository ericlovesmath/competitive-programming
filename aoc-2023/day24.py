import numpy as np
from z3 import Int, Solver, sat

with open("day24.in") as f:
    inp = f.read().strip().splitlines()

# I literally installed Z3 just for this problem

hail = []
for row in inp:
    l, r = row.split(" @ ")
    l = [int(num) for num in l.split(", ")]
    r = [int(num) for num in r.split(", ")]
    hail.append([l, r])

lower, upper = 2e14, 4e14
count = 0
for (x1, y1, _), (vx1, vy1, _) in hail:
    for (x2, y2, _), (vx2, vy2, _) in hail:
        m1, m2 = vy1 / vx1, vy2 / vx2
        if m1 == m2:
            continue
        A = np.array([[m1, -1], [m2, -1]])
        b = np.array([m1 * x1 - y1, m2 * x2 - y2])
        x, y = np.linalg.solve(A, b)
        if 2e14 <= x <= 4e14 and 2e14 <= y <= 4e14:
            if (x - x1) / vx1 > 0 and (x - x2) / vx2 > 0:
                count += 1
count //= 2
print("Part 1:", count)

# Only have to check first 3 hailstones to define unique line
solver = Solver()
x, y, z, vx, vy, vz = [Int(var) for var in ("x", "y", "z", "vx", "vy", "vz")]
for i, [(a, b, c), (va, vb, vc)] in enumerate(hail[:3]):
    t = Int(f"t_{i}")
    solver.add(t > 0)
    solver.add(x + vx * t == a + va * t)
    solver.add(y + vy * t == b + vb * t)
    solver.add(z + vz * t == c + vc * t)
assert solver.check() == sat
print("Part 2:", sum(solver.model().eval(var).as_long() for var in (x, y, z)))
