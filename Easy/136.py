def singleNumber(nums):
    temp = []
    for i in nums:
        if i not in temp:
            temp.append(i)
        elif i in temp:
            temp.remove(i)
    return temp[0]

nums = [4,1,2,1,2]
print(singleNumber(nums))