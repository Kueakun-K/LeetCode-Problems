def isValid(s: str) -> bool:
    def checkMatch(s1, s2):
        if (s1 == '(' and s2 == ')') or (s1 == '{' and s2 == '}') or (s1 == '[' and s2 == ']'):
            return True
        else:
            return False
    openParentheses = ['(', '{', '[']
    stackParentheses = []
    for i in s:
        ans = False
        if i in openParentheses:
            stackParentheses.append(i)
        elif i not in openParentheses:
            if not stackParentheses:
                return False
            ans = checkMatch(stackParentheses[-1], i)
            if ans:
                stackParentheses.pop(-1)
            else:
                return False
    return stackParentheses == []

s = "(])"
print(isValid(s))