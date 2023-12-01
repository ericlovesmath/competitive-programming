with open("day01.in") as f:
    inp = f.read().strip()

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
words = {words[i]: i + 1 for i in range(9)}

ans = 0
for row in inp.split():
    i = 0
    digits = []
    while i < len(row):
        if row[i].isdigit():
            digits.append(int(row[i]))
        i += 1

    ans += digits[0] * 10 + digits[-1]
print(ans)


ans = 0
for row in inp.split():
    i = 0

    tens = 0
    while i < len(row) and tens == 0:
        if row[i].isdigit():
            tens += int(row[i])
        else:
            for w in words:
                if row[i:].startswith(w):
                    tens += words[w]
                    break
        i += 1

    i = len(row) - 1
    ones = 0
    while i >= 0 and ones == 0:
        if row[i].isdigit():
            ones += int(row[i])
        else:
            for w in words:
                if row[:i + 1].endswith(w):
                    ones += words[w]
                    break
        i -= 1

    ans += tens * 10 + ones
print(ans)
