def addDigits(num):
    while num >= 10:
        temp = 0
        for i in str(num):
            temp += int(i)
        num = temp
    return num
num = 38
print(addDigits(num))