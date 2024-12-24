from functools import lru_cache

with open("day24.in") as f:
    inp = f.read().strip().split("\n\n")
    inits = {}
    for row in inp[0].splitlines():
        l, r = row.split()
        inits[l[:-1]] = (r == "1")
    conns = {}
    for row in inp[1].splitlines():
        a, rule, b, _, c = row.split()
        conns[c] = (a, rule, b)

@lru_cache
def get_val(node):
    if node in inits:
        return inits[node]

    a, rule, b = conns[node]
    match rule:
        case "AND":
            return get_val(a) and get_val(b)
        case "OR":
            return get_val(a) or get_val(b)
        case "XOR":
            return get_val(a) ^ get_val(b)

    assert False


res = []
for i in range(1000):
    z = f"z{i:02}"
    if z not in conns:
        break
    res.append(get_val(z))

ans = 0
for bit in reversed(res):
    ans = ans * 2 + int(bit)

print(ans)

# Part 2 was done manually. On an iPad. Do not ask me to explain. It sucked.
