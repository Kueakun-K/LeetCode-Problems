def convert(s: str, numRows: int) -> str:
    if numRows > 1:
        table = []
        output = ""
        for i in range(numRows):
            table.append([])
        pt = 0
        direction = True
        for i in s:
            table[pt].append(i)
            if pt == 0:
                direction = True
            elif pt == numRows - 1:
                direction = False
            if direction:
                pt += 1
            else:
                pt -= 1
        for i in table:
            for j in i:
                output += j
        return output
    else:
        return s

s = "PAYPALISHIRING" 
numRows = 4
print(convert(s, numRows))