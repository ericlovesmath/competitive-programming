with open("day25.in") as f:
    inp = f.read().strip().splitlines()


def SNAFUToDecimal(num):
    ans = 0
    digit_map = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    for dig in num:
        ans = ans * 5 + digit_map[dig]
    return ans


def DecimalToSNAFU(num):
    # Idea is to add 2 to at least each digit in SNAFU form
    # Then convert as if it is normal base 5

    num_digits = 0
    while 5 ** num_digits < num:
        num_digits += 1

    num += int("2" * num_digits, 5)
    base_five = []
    while num:
        base_five.append(num % 5)
        num //= 5

    ans = ["=-012"[dig] for dig in base_five[::-1]]
    return "".join(ans).lstrip("0")


print(DecimalToSNAFU(sum(map(SNAFUToDecimal, inp))))
