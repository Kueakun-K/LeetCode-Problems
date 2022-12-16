def singleNumber(nums):
    temp = []
    for i in nums:
        if i not in temp:
            temp.append(i)
        elif i in temp:
            temp.remove(i)
    return temp

nums = [1,2,1,3,2,5]
print(singleNumber(nums))