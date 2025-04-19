from typing import List
def countFairPairs(nums: List[int], lower: int, upper: int) -> int:
    nums.sort()
    count = 0
    n = len(nums)
    j1 = j2 = n - 1
    for i in range(n):
        while j1 > i and nums[i] + nums[j1] > upper:
            j1 -= 1
        while j2 > i and nums[i] + nums[j2] >= lower:
            j2 -= 1
        count += max(0, j2 - max(i + 1, j1 + 1) + 1)
    return count

nums = [-5,-5,-5,-7,-7]
lower = -12
upper = -12
print(countFairPairs(nums, lower, upper))