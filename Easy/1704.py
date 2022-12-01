def halvesAreAlike(s: str) -> bool:
    anum = bnum = 0
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(s)):
        if i < len(s)/2:
            if s[i] in vowel:
                anum += 1
        else:
            if s[i] in vowel:
                bnum += 1
    if anum == bnum:
        return True
    else: return False
        
s = "textbook"
print(halvesAreAlike(s))