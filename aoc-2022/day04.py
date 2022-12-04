import re

with open("day04.in") as f:
    inp = f.read().strip().split("\n")
    inp = [list(map(int, re.split(r'\D+', row))) for row in inp]

print(sum(1 for row in inp
          if (row[0] <= row[2] and row[1] >= row[3])
          or (row[0] >= row[2] and row[1] <= row[3])))

print(sum(1 for row in inp
          if not (row[1] < row[2] or row[0] > row[3])))
