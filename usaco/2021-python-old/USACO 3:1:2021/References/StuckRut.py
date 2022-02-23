"""
ID: dazzlethelightwing
LANG: PYTHON3
TASK: Stuck In A Rut
"""
import math

n = int(input())
cows = []
for i in range(n):
    inp = input().split()
    if inp[0] == "E":
        direction = 1 # x positive
    else:
        direction = 2 # y positive
    cows.append([direction, int(inp[1]), int(inp[2])])

print(cows)

# record past cow paths
for j in range(2):
    past_cow_paths = []
    past_cow_paths.extend(cows)

    # next step
    for i, cow in enumerate(cows):
        cows[i][cow[0]] += 1
        
        is_repeat = False
        for past_cow in past_cow_paths:
            if cow == past_cow:
                is_repeat = True
        
        if is_repeat:
            del[cows[cow[0]]]

print(cows)


# Notes

somelist.sort(key=lambda x: x[2]) # sorts list by second item in sub lists


