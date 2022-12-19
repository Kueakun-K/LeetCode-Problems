def searchRange(nums, target): #with Olon(n) algorithm
    def findRight():
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def findLeft():
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    rightBorder = findRight()
    leftBorder = findLeft()
    print([leftBorder, rightBorder])
    return [leftBorder, rightBorder] if rightBorder >= leftBorder else [-1, -1]

nums = [1] 
target = 1
print(searchRange(nums, target))