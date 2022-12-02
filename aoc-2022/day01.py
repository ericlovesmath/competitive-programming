with open("day01.in") as f:
    inp = f.read().strip()

a = sorted(sum(map(int, elf.split("\n"))) for elf in inp.split("\n\n"))

print(a[-1])
print(sum(a[-3:]))
