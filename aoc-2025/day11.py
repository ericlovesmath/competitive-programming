from functools import lru_cache

with open("day11.in") as f:
    inp = f.read().strip().splitlines()
    graph = {}
    for row in inp:
        src, *dsts = row.split()
        graph[src[:-1]] = dsts
    N = len(graph)


@lru_cache
def search(src, dst, without):
    if src == dst:
        return 1
    if src in without:
        return 0
    return sum(search(out, dst, without) for out in graph[src])


print(search("you", "out", ()))

print(
    search("svr", "fft", ("dac", "out"))
    * search("fft", "dac", ("svr", "out"))
    * search("dac", "out", ("svr", "fft"))
    + (
        search("svr", "dac", ("fft", "out"))
        * search("dac", "fft", ("svr", "out"))
        * search("fft", "out", ("svr", "dac"))
    )
)
