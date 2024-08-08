def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart:int):
    ans = []
    rowChange = 1
    colChange = 1
    ans.append([rStart, cStart])
    while len(ans) < rows * cols:
        colChange += 1
        for i in range(1, colChange):
            cStart += 1
            if 0 <= rStart < rows and 0 <= cStart < cols:
                ans.append([rStart,cStart])
        rowChange += 1
        for i in range(1, rowChange):
            rStart += 1
            if 0 <= rStart < rows and 0 <= cStart < cols:
                ans.append([rStart,cStart])
        colChange += 1
        for i in range(1, colChange):
            cStart -= 1
            if 0 <= rStart < rows and 0 <= cStart < cols:
                ans.append([rStart,cStart])
        rowChange += 1
        for i in range(1, rowChange):
            rStart -= 1
            if 0 <= rStart < rows and 0 <= cStart < cols:
                ans.append([rStart,cStart])
    return ans

rows = 5
cols = 6
rStart = 1
cStart = 4
print(spiralMatrixIII(rows, cols, rStart, cStart))