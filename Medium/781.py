from typing import List
def numRabbits(answers: List[int]) -> int:
    count = 0
    temp = [0] * (max(answers) + 1)
    for i in range(len(answers)):
        if answers[i] == 0:
            count += 1
        else:
            temp[answers[i]] += answers[i]
    print(temp)
    for j in range(1, len(temp)):
        if temp[j] == 0:
            pass
        elif (temp[j] // j) // (j + 1) > 0:
            count += (j + 1) * ((temp[j] // j) // (j + 1))
            if temp[j] % (j + 1) > 0:
                count += (j + 1)
        else:
            count += (j + 1)
    return count

answers = [0,3,2,0,3,3,4,2,4,3,2,4,4,3,0,1,3,4,4,3]
print(numRabbits(answers))