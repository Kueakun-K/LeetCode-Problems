def rangeSum(nums, n, left, right):
    sumarraySum = []
    index = 0
    temp = 1
    for i in range(int(n * (n + 1) / 2)):
        if temp < n + 1:
            sumarraySum.append(sum(nums[index:temp]))
            temp += 1
        else:
            index += 1
            temp = index + 1
            sumarraySum.append(sum(nums[index:temp]))
            temp += 1
    sumarraySum.sort()
    mod = 10**9 + 7
    return sum(sumarraySum[left - 1:right]) % mod

nums = [1,2,3,4]
n = 4
left = 1
right = 5
print(rangeSum(nums, n, left, right))