def removeDuplicates(nums:list):
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))