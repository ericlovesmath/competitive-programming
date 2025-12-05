with open("day08.in") as f:
    inp = f.read().strip().splitlines()

a = { "".join(sorted("abc")): 1 }

count = 0
for row in inp:
    sig, out = row.split("|")
    print(out)
    out = [ "".join(sorted(i)) for i in out.split()]
    for n in out:
        print(n)
        print(identify[n])
        if len(n) in set([2, 4, 3, 7]):
            count += 1

print(count)
