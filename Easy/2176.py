from typing import List
def countPairs(nums: List[int], k: int) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != -1 and i != j and nums[i] == nums[j]:
                if (i * j) % k == 0:
                    count += 1
        nums[i] = -1
    return count

nums = [84, 26, 33, 26, 27, 35, 56, 18, 51, 22]
k = 2
print(countPairs(nums, k))