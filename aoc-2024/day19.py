from functools import lru_cache

with open("day19.in") as f:
    choices, _, *designs = f.read().strip().splitlines()
    choices = choices.split(", ")


# Pure functions can be cached, DP is overkill
@lru_cache(maxsize=None)
def check(design):
    if design == "":
        return 1

    count = 0
    for choice in choices:
        N = len(choice)
        if design[:N] == choice:
            count += check(design[N:])
    return count


scores = [check(design) for design in designs]
print(sum(s > 0 for s in scores))
print(sum(scores))
