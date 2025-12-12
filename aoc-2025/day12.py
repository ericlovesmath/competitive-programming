# NOTE: Turns out none of this is necessary, the input just cares if the size is big enough.
# The shapes fit the whole rectangle or they don't.

with open("day12.in") as f:
    *raw_shapes, raw_regions = f.read().strip().split("\n\n")

    shapes = []
    for raw_shape in raw_shapes:
        shape = raw_shape.splitlines()[1:]
        shape = [(i, j) for i in range(3) for j in range(3) if shape[i][j] == "#"]
        shape = frozenset(shape)

        variants = set()
        for _ in range(4):
            flipped = frozenset((r, c) for r, c in shape)
            rotated = frozenset((c, -r) for r, c in shape)
            variants.add(flipped)
            variants.add(rotated)
            shape = rotated

        shapes.append(list(variants))

    regions = []
    for region in raw_regions.splitlines():
        size, *counts = region.split()
        regions.append((int(size[:2]), int(size[3:5]), tuple(map(int, counts))))


def solve_region(w, h, pieces):
    if sum(len(p[0]) for p in pieces) > w * h:
        return False

    def backtrack(idx, filled):
        if idx == len(pieces):
            return True

        for var in pieces[idx]:
            for r in range(h):
                for c in range(w):
                    valid = all(0 <= r + dr < h and 0 <= c + dc < w and (r + dr, c + dc) not in filled 
                               for dr, dc in var)
                    if valid:
                        new_filled = filled | {(r+dr, c+dc) for dr, dc in var}
                        if backtrack(idx + 1, new_filled):
                            return True
        return False

    return backtrack(0, set())


count = 0
for w, h, counts in regions:
    pieces = [shape for i, c in enumerate(counts) for shape in [shapes[i]] * c]
    if solve_region(w, h, pieces):
        count += 1

print(count)
