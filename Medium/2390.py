def removeStars(s: str) -> str:
    stack = []
    for i in s:
        if i == "*":
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)

s = "leet**cod*e"
print(removeStars(s))