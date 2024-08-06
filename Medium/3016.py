def miniumPushes(word:str):
    wordFrequency = [0] * 26
    for i in word:
        wordFrequency[ord(i) - ord("a")] += 1
    wordFrequency.sort(reverse=True)
    ans = 0
    for i in range(26):
        if wordFrequency[i] == 0:
            break
        ans += (wordFrequency[i] * (i//8 + 1))
    return ans

word = "aabbccddeeffgghhiiiiii"
print(miniumPushes(word))