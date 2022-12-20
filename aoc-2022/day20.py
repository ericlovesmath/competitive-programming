class Node:
    """Circular Linked List"""

    def __init__(self, val: int):
        self.val = val
        self.left: Node
        self.right: Node


with open("day20.in") as f:
    inp = [Node(int(val) * 811589153) for val in f.read().strip().splitlines()]

for i in range(len(inp)):
    inp[i].left = inp[(i - 1) % len(inp)]
    inp[i].right = inp[(i + 1) % len(inp)]

for _ in range(10):
    for curr in inp:
        if curr.val == 0:
            zero_node = curr
            continue

        source_left = curr.left
        source_right = curr.right

        if curr.val > 0:
            for _ in range(curr.val % (len(inp) - 1)):
                curr.right = curr.right.right
            curr.left = curr.right.left
        else:
            for _ in range(-curr.val % (len(inp) - 1)):
                curr.left = curr.left.left
            curr.right = curr.left.right

        curr.left.right = curr
        curr.right.left = curr
        source_left.right = source_right
        source_right.left = source_left

start = zero_node
ANS = 0
for i in range(3000):
    start = start.right
    if (i + 1) % 1000 == 0:
        ANS += start.val
print(ANS)
