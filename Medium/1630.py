from typing import List
def checkArithmeticSubarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    ans = []
    for i in range(len(l)):
        subArray = nums[l[i]:r[i] + 1]
        subArray.sort()
        bef = subArray[0]
        gap = subArray[1] - bef
        for j in range(1, len(subArray)):
            if j == len(subArray) - 1 and subArray[j] - bef == gap:
                ans.append(True)
            elif subArray[j] - bef == gap:
                bef = subArray[j]
            else:
                ans.append(False)
                break
    return ans

nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]
print(checkArithmeticSubarrays(nums, l, r))