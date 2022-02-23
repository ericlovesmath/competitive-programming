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
    while len(paint) > 1:
        # Remove adjacent duplicates
        paint[:] = [n for i, n in enumerate(paint)
                     if i==0 or n != paint[i-1]]

        #print(thin_paint)
        #print(max(paint))
        
        count += paint.count(max(paint))
        paint[:] = [i for i in paint if i != max(paint)]
    
    return(count + len(paint))

for ex_range in ranges:
    print(stroke_count(paint[:ex_range[0]-1])+
          stroke_count(paint[ex_range[1]:]))
    