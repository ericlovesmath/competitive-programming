import os

script_dir = os.path.dirname(__file__)

with open(os.path.join(script_dir, "day06.in")) as f:
    inp = f.read().strip()

SIZE = 14

for i in range(len(inp)):
    if len(set(inp[i : i + SIZE])) == SIZE:
        print(i + SIZE)
        break
