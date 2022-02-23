"""
ID: dazzlethelightwing
LANG: PYTHON3
TASK: Rectangular Pasture
"""
import math

n = int(input())
cows = [[int(coord) for coord in input().split()] for i in range(n)]

count = 0

for bin_subset in range(1,2**n):
    subset = bin(bin_subset)[2:].zfill(n)
    # subset = 0100
    #print(subset)
    
    x_list = [coord[0] for i, coord in enumerate(cows) if subset[i] == "1"]
    y_list = [coord[1] for i, coord in enumerate(cows) if subset[i] == "1"]

    is_bounding_box = True
    for i in range(n):
        if subset[i] == "0":
            if min(x_list) < cows[i][0] < max(x_list) + 1 and min(y_list) < cows[i][1] < max(y_list) + 1:
                is_bounding_box = False
    
    if is_bounding_box:
        count += 1
        #print(subset)
        #print(x_min, x_max, y_min, y_max)
        
        
#print("\n")
#print(n)
#print(cows)
print(count + 1)