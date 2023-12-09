with open("day09.in") as f:
    inp = f.read().strip().splitlines()
    inp = [[int(d) for d in row.split()] for row in inp]

def get_next(row):
    last = 0
    for i in range(len(row) - 1, 0, -1):
        last += row[i]
        row = [row[j + 1] - row[j] for j in range(i)]
    return last + row[0]

print(sum(get_next(row) for row in inp))
print(sum(get_next(row[::-1]) for row in inp))
