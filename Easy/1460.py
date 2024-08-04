def canBeEqual(target:list, arr:list):
    if len(target) != len(arr):
        return False
    target.sort()
    arr.sort()
    if target != arr:
        return False
    return True

target = [1,2,3,4]
arr = [2,4,1,3]
print(canBeEqual(target, arr))