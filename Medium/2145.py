from typing import List
def numberOfArrays(differences: List[int], lower: int, upper: int) -> int:
    hidden = [0] * (len(differences) + 1)
    hidden[0] = minNum = maxNum = lower
    for i in range(len(differences)):
        hidden[i + 1] = hidden[i] + differences[i]
        if hidden[i + 1] < minNum:
            minNum = hidden[i + 1] 
        elif hidden[i+ 1] > maxNum:
            maxNum = hidden[i + 1]
    if (maxNum + (lower - minNum)) > upper:
        return 0
    else:
        return (upper - (maxNum + (lower - minNum))) + 1

differences = [1,-3,4]
lower = 1
upper = 6
print(numberOfArrays(differences, lower, upper))