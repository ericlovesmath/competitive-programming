"""
ID: dazzlethelightwing
LANG: PYTHON3
TASK: NoTimeToPaint
"""
N, Q = map(int, input().split(" "))
paint = [ord(char) - 96 for char in input().lower()]
ranges = [list(map(int, input().split(" "))) for i in range(Q)]
#print(N, Q)
#print(paint)
#print(ranges)

def stroke_count(paint):
    count = 0
    
    if len(paint) == 0:
        return 0
    
    is_upward = False
    is_downward = False
    
    #print(paint)
    
    curve_ids = [0]
    for i in range(1,len(paint)):
        if paint[i] < paint[i-1]:
            is_downward = True
            is_upward = False
        elif paint[i] > paint[i-1]:
            if is_downward:
                is_downward = False
                curve_ids.append(i-1)
            is_upward = True
    curve_ids.append(len(paint)-1)
    
    count = 0
    for i in range(len(curve_ids) - 1):
        hill = paint[curve_ids[i]:curve_ids[i+1]+1]
        count += len(set(hill))
    
    return count

for ex_range in ranges:
    #print("")
    #print(stroke_count(paint[:ex_range[0]-1]))
    #print(stroke_count(paint[ex_range[1]:]))
    print(stroke_count(paint[:ex_range[0]-1])+
          stroke_count(paint[ex_range[1]:]))

#print(stroke_count([1, 1, 2, 2, 3, 4, 7, 7, 6, 5, 7, 8, 9, 9, 8, 1, 1, 2, 4, 3, 5, 2, 1]))
    