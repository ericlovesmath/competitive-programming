with open("day06.in") as f:
    inp = [int(i) for i in f.read().strip().split(",")]

fish = [inp.count(i) for i in range(9)]

for _ in range(256):
    next = fish[1:] + fish[:1]
    next[6] += fish[0]
    fish = next

print(sum(fish))
