import re
from functools import cache

with open("day12.in") as f:
    inp = f.read().strip().splitlines()

# Part 1: Rank 167
# Naive, Brute force solution

def swaps(s):
    if "?" not in s:
        yield s
    else:
        i = s.index("?")
        yield from swaps(s[:i] + "." + s[i+1:])
        yield from swaps(s[:i] + "#" + s[i+1:])

ans = 0
for row in inp:
    field, widths = row.split()
    widths = [int(n) for n in widths.split(",")]
    for s in swaps(field):
        if [len(n) for n in re.findall(r"\#+", s)] == widths:
            ans += 1
print(ans)

# Part 2: Rank 146
# I'm not incredibly happy with my solution but its basically "DP"
# We will repeat more often than not so caching is a massive benefit
# Runs in less than 5 seconds, so as far as I'm concerned...

@cache
def valid(field, widths, count):
    if field == "":
        return (len(widths) == 0 and count == 0) or (len(widths) == 1 and count == widths[0])
    if field[0] == "#":
        return valid(field[1:], widths, count + 1)
    elif field[0] == ".":
        if count == 0:
            return valid(field[1:], widths, 0)
        elif len(widths) != 0 and widths[0] == count:
            return valid(field[1:], widths[1:], 0)
        return 0
    else:
        return valid("#" + field[1:], widths, count) + valid("." + field[1:], widths, count)

ans = 0
for i, row in enumerate(inp):
    field, widths = row.split()
    field = field + "?" + field + "?" + field + "?" + field + "?" + field
    widths = [int(n) for n in widths.split(",")] * 5
    ans += valid(field, tuple(widths), 0)
print(ans)
