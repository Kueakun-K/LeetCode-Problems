def singleNumber(nums):
    temp = []
    temp2 = []
    for i in nums:
        if i not in temp:
            temp.append(i)
        elif i in temp:
            if i in temp2:
                temp.remove(i)
            else:
                temp2.append(i)
    return temp[0]

nums = [0,1,0,1,0,1,99]
print(singleNumber(nums))