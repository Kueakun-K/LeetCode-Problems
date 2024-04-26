def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]

nums = [3,2,3]
print(majorityElement(nums))