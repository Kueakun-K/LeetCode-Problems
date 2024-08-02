def minSwaps(nums:list):
    k = nums.count(1)
    mx = cnt = sum(nums[:k])
    n = len(nums)
    for i in range(1,n):
        if i + k <= n:
            cnt += nums[i + k - 1]
            cnt -= nums[i - 1]
        else:
            cnt += nums[(i + k) - n - 1]
            cnt -= nums[i - 1]
        mx = max(cnt, mx)
    return k - mx

nums = [0,1,0,1,1,0,0]
# nums = [1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0]
print(minSwaps(nums))