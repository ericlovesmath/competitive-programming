with open("day07.in") as f:
    inp = f.read().strip().splitlines()

def test(nums: list[int]):
    if len(nums) == 1:
        return nums
    *nums, back = nums
    res = []
    for n in test(nums):
        res.append(n + back)
        res.append(n * back)
        res.append(int(str(n) + str(back)))
    return res

count = 0
for row in inp:
    total, nums = row.split(":")
    total = int(total)
    nums = [int(i) for i in nums.strip().split()]
    if total in test(nums):
        count += total

print(count)
