"""
ID: dazzlethelightwing
LANG: PYTHON3
TASK: DanceMooves
"""
import math

n, k = map(int, input().split(" "))

move_list = [{} for i in range(n)]

for i in range(k):
    line = list(map(int, input().split(" ")))
    move_list[line[0]-1][i] = line[1]-1
    move_list[line[1]-1][i] = line[0]-1

#print(n, k)
#print(move_list)

def cow_positions(curr, time, past_pos):
    #print(curr, time, past_pos)
    if time >= 5*k:
        return len(set(past_pos))
    
    for i in range(k):
        if ((time+i)%k) in move_list[curr]:
            return cow_positions(move_list[curr][(time+i)%k],
                                time+1+i, past_pos + [move_list[curr][(time+i)%k]])
            
    return(len(set(past_pos)))

for i in range(n):
    print(cow_positions(i, 0, [i]))
    #print("\n")
