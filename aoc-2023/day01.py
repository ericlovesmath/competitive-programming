with open("day01.in") as f:
    inp = f.read().strip().split("\n")

ans = 0
for row in inp:
    digits = [int(c) for c in row if c.isdigit()]
    ans += digits[0] * 10 + digits[-1]
print(ans)

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
words = {words[i]: i + 1 for i in range(9)}

ans = 0
for row in inp:
    tens = 0
    for i in range(len(row)):
        if tens != 0:
            break
        if row[i].isdigit():
            tens += int(row[i])
        for w in words:
            if row[i:].startswith(w):
                tens += words[w]

    ones = 0
    for i in range(len(row) - 1, -1, -1):
        if ones != 0:
            break
        if row[i].isdigit():
            ones += int(row[i])
        for w in words:
            if row[:i + 1].endswith(w):
                ones += words[w]

    ans += tens * 10 + ones
print(ans)
