def twoSum(numbers, target):
    leftIndex = 0
    rightIndex = len(numbers) - 1
    while rightIndex >= leftIndex:
        sum = numbers[leftIndex] + numbers[rightIndex]
        if sum == target:
            return [leftIndex + 1, rightIndex + 1]
        if sum > target:
            rightIndex -= 1
        else:
            leftIndex += 1

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))