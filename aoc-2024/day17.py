import re

with open("day17.in") as f:
    inp = f.read().strip()
    A, B, C, *program = [int(i) for i in re.findall(r"-?\d+", inp)]

def combo(n):
    return [0, 1, 2, 3, A, B, C, None][n]

pc = 0
out = []
while pc < len(program):
    op, val = program[pc], program[pc + 1]
    div = (A // (2 ** combo(val)))
    match op:
        case 0:
            A = div
        case 1:
            B ^= val
        case 2:
            B = combo(val) % 8
        case 3:
            if A != 0:
                pc = val - 2
        case 4:
            B ^= C
        case 5:
            out.append(combo(val) % 8)
        case 6:
            B = div
        case 7:
            C = div
    pc += 2

print(",".join([str(s) for s in out]))

# Program: 2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0
# Manually simplified program. Painful. But needed
# This shows that each output depends on 3 bit blocks of A
def test(A):
    B = 0

    res = []
    while A != 0:
        B = A % 8
        B = B ^ 3 ^ (A >> (B ^ 5))
        A = A >> 3
        res.append(B % 8)
    return res

# We can bash for each 3 bit block "a" instead of all A
def solve(program, i, A):
    for a in range(8):
        A2 = (A << 3) + a
        if test(A2) == program[i:]:
            if i == 0:
                return A2
            next = solve(program, i - 1, A2)
            if next is not None:
                return next
    return None

print(solve(program, len(program) - 1, 0))
