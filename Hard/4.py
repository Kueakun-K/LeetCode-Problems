from typing import List
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        merged = []
        lenlist = len(nums1) + len(nums2)
        for i in nums1:
            merged.append(i)
        for j in nums2:
            merged.append(j)
        merged.sort()
        if lenlist % 2 == 0:
            x = lenlist / 2
            ans = (merged[int(x-1)] + merged[int(x)]) / 2
        else:
            x = (lenlist / 2) - 0.5
            ans = merged[int(x)]
        return ans

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))