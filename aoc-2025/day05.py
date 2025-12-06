with open("day05.in") as f:
    ranges, ids = f.read().strip().split("\n\n")
    ranges = [s.split("-") for s in ranges.splitlines()]
    ranges = [(int(l), int(r)) for [l, r] in ranges]
    ids = [int(n) for n in ids.splitlines()]

print(sum(any(l <= n <= r for (l, r) in ranges) for n in ids))


def compress(ranges):
    next = []
    curr = ranges[0]
    for i in range(1, len(ranges)):
        (x, y), (l, r) = curr, ranges[i]
        if l <= y:
            curr = (x, max(r, y))
        else:
            next.append(curr)
            curr = (l, r)
    next.append(curr)
    return next


def fix_compress(ranges):
    next = compress(ranges)
    if len(next) == len(ranges):
        return next
    return fix_compress(next)


print(sum(r - l + 1 for (l, r) in fix_compress(sorted(ranges))))
