with open("day04.in") as f:
    draws, *boards = f.read().strip().split("\n\n")

draws = [int(i) for i in draws.split(",")]
boards = [[int(i) for i in board.split()] for board in boards]
N = len(boards)

marks = [[False for _ in range(25)] for _ in range(N)]

def checks():
    for i in range(5):
        yield [5 * i, 5 * i + 1, 5 * i + 2, 5 * i + 3, 5 * i + 4]
        yield [0 + i, 5 + i, 10 + i, 15 + i, 20 + i]


def check(board):
    for line in checks():
        if all(board[sq] for sq in line):
            return True
    return False


done = set()

for draw in draws:
    next = []
    for i in range(N):
        if i in done:
            continue
        for loc in range(25):
            if boards[i][loc] == draw:
                marks[i][loc] = True
        if check(marks[i]):
            res = 0
            for loc in range(25):
                if not marks[i][loc]:
                    res += boards[i][loc]
            print(res * draw)
            done.add(i)
