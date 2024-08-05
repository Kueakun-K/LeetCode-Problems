def kthDistinct(arr:list, k):
    distinctArr = []
    for i in arr:
        if arr.count(i) == 1:
            distinctArr.append(i)
    print(distinctArr)
    if len(distinctArr) >= k:
        return distinctArr[k - 1]
    return ""

arr = ["aaa","aa","a"]
k = 1
print(kthDistinct(arr, k))