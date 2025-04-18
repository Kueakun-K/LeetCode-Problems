def recursive(i, n, say):
    if n == 1:
        return "1"
    elif n == 2:
        return "11"
    elif i == 0:
        say = "1"
        return recursive(i+1, n, say)
    elif i == 1:
        say ="11"
        return recursive(i+1, n, say)
    elif i < n:
        temp = say[0]
        count = 0
        word = ""
        for j in say:
            if temp == j:
                count += 1
            else:
                word += str(count)
                word += temp
                temp = j
                count = 1
        if count >= 1:
            word += str(count)
            word += temp
        return recursive(i+1, n, word)
    else:
        return say
def countAndSay(n: int) -> str:
    say = ""
    say = recursive(0, n, say)
    return say

n = 4
print(countAndSay(n))