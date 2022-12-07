import os

script_dir = os.path.dirname(__file__)

with open(os.path.join(script_dir, "day07.in")) as f:
    inp = f.read().strip().split("\n")

filesystem = {"/": {}}
loc = ["/"]

pos = 0
while pos < len(inp):
    _, cmd, *args = inp[pos].split()
    if cmd == "cd":
        match args[0]:
            case "/":
                loc = ["/"]
            case "..":
                loc.pop()
            case _:
                loc.append(args[0])
    if cmd == "ls":
        curr = filesystem
        for path in loc:
            curr = curr[path]
        while pos + 1 < len(inp) and inp[pos + 1][0] != "$":
            size, file = inp[pos + 1].split()
            if size == "dir":
                curr[file] = {}
            else:
                curr[file] = int(size)
            pos += 1
    pos += 1

# Get Sizes

dirs = []

def size(folder, items):
    if isinstance(items, dict):
        total = sum(size(item, items[item]) for item in items)
        dirs.append((folder, total))
        return total
    else:
        return items

size("/", filesystem)

# Problem 1

print(sum(size for dir, size in dirs if size <= 100000))

# Problem 2

dirs.sort(key=lambda x: x[1])
for dir, size in dirs:
    if size >= dirs[-1][1] - 40000000:
        print(size)
        break
