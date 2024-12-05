with open("day05.in") as f:
    _rules, _pages = f.read().strip().split("\n\n")
    rules = [(int(rule[:2]), int(rule[3:])) for rule in _rules.splitlines()]
    pages = [[int(i) for i in page.split(",")] for page in _pages.splitlines()]

def check(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[j], nums[i]) in rules:
                return False
    return True

def swap(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[j], nums[i]) in rules:
                nums[j], nums[i] = nums[i], nums[j]
    return nums

print(sum(nums[len(nums) // 2] for nums in pages if check(nums)))
print(sum(swap(nums)[len(nums) // 2] for nums in pages if not check(nums)))
