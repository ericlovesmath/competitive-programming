with open("day25.in") as f:
    inp = f.read().strip().split("\n\n")
    inp = [block.splitlines() for block in inp]

keys = []
locks = []
for r in inp:
    if all(x == "#" for x in r[0]):
        assert all(x != "#" for x in r[-1])
        locks.append(r)
    else:
        keys.append(r)


count = 0
for lock in locks:
    for key in keys:
        for j in range(5):
            lockpin = sum(lock[i][j] == "#" for i in range(7))
            keypin = sum(key[i][j] == "#" for i in range(7))
            if lockpin + keypin >= 8:
                break
        else:
            count += 1

print(count)
