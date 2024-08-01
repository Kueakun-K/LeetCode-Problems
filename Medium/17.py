def letterCombinations(digits):
    keyboard = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
    }
    ans = []
    if len(digits) == 0:
        return ans
    elif len(digits) == 1:
        for i in range(len(keyboard[digits[0]])):
            ans.append(keyboard[digits[0]][i])
        return ans
    elif len(digits) == 2:
        for i in range(len(keyboard[digits[0]])):
            for j in range(len(keyboard[digits[1]])):
                ans.append(keyboard[digits[0]][i] + keyboard[digits[1]][j])
        return ans
    elif len(digits) == 3:
        for i in range(len(keyboard[digits[0]])):
            for j in range(len(keyboard[digits[1]])):
                for k in range(len(keyboard[digits[2]])):
                    ans.append(keyboard[digits[0]][i] + keyboard[digits[1]][j] + keyboard[digits[2]][k])
        return ans
    elif len(digits) == 4:
        for i in range(len(keyboard[digits[0]])):
            for j in range(len(keyboard[digits[1]])):
                for k in range(len(keyboard[digits[2]])):
                    for l in range(len(keyboard[digits[3]])):
                        ans.append(keyboard[digits[0]][i] + keyboard[digits[1]][j] + keyboard[digits[2]][k] + keyboard[digits[3]][l])
        return ans
    

digits = "2366"
print(letterCombinations(digits))