from typing import List
def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    num = 0
    while num != len(popped):
        if not pushed and stack[-1] != popped[num]:
            return False
        elif stack and stack[-1] == popped[num]:
            stack.pop()
            num += 1
        else:
            stack.append(pushed.pop(0))
    return True

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(validateStackSequences(pushed, popped))