"""
ID: dazzlethelightwing
LANG: PYTHON3
TASK: Comfortable Cows
"""
import math
import pprint
pp = pprint.PrettyPrinter(indent=4)

N = int(input())
cow_coords = [tuple(map(int,input().split())) for i in range(N)]
#N = 9
#cow_coords = [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1)]

#print(N)
#print(cow_coords)

def near(cow, cows):
    return (
        (cow[0]+1,cow[1]) in cows,
        (cow[0],cow[1]+1) in cows,
        (cow[0]-1,cow[1]) in cows,
        (cow[0],cow[1]-1) in cows
    )
def near_coords(cow):
    return (
        (cow[0]+1,cow[1]),
        (cow[0],cow[1]+1),
        (cow[0]-1,cow[1]),
        (cow[0],cow[1]-1)
    )

def is_comfy(cow, cows):
    return(sum(bool(x) for x in near(cow, cows))==3) 

def first_i_count(cows):
    count = 0
    for cow in cows:
        if is_comfy(cow, cows):
            cows.append(near_coords(cow)[near(cow, cows).index(False)])
            count += 1
    print(count)
    
for i in range(1,N+1):
    first_i_count(cow_coords[:i])


