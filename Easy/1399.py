def countLargestGroup(n: int) -> int:
    group = [0] * (n + 1)
    maxNum = 0
    count = 0
    for i in range(1, n + 1):
        if i < 10:
            temp = i
            group[temp] += 1
        elif i < 100:
            temp = (i // 10) + (i % 10)
            group[temp] += 1
        elif i < 1000:
            temp = (i // 100) + ((i // 10) % 10) + (i % 10)
            group[temp] += 1   
        else:
            temp = (i // 1000) + ((i // 100) % 10) + ((i // 10) % 10) + (i % 10)
            group[temp] += 1 
        if group[temp] > maxNum:
            maxNum = group[temp]
            count = 1
        elif group[temp] == maxNum:
            count += 1
    return count
n = 46
print(countLargestGroup(n))