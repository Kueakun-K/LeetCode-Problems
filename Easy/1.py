from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                break
        return [i,nums.index(diff)]
    
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))