def mySqrt(x: int) -> int:
    if x > 1:
        for i in range(x+1):
            if i*i > x:
                return i - 1 
            elif i*i == x:
                return i
    else: return x

x = 3
print(mySqrt(x))