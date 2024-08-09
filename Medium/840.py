def numMagicSquaresInside(grid: list[list[int]]):
    def isMagic(i, j):
        once=[False]*10
        rowSum=[0]*3
        colSum= [0]*3
        for a in range(i-1, i+2):
            for b in range(j-1, j+2):
                x= grid[a][b]
                if x < 1 or x > 9: return False
                rowSum[a-i+1] += x
                colSum[b-j+1] += x
                if once[x]: 
                    return False 
                once[x]=True
        for b in once[1:]: 
            if not b: return False
        for sum in rowSum:
            if sum!=15: return False
        for sum in colSum:
            if sum!=15: return False
        return grid[i-1][j-1]+grid[i+1][j+1]==10 and grid[i+1][j-1]+grid[i-1][j+1]==10
    
    if len(grid) < 3 or len(grid[0]) < 3:
        return 0
    ans = 0
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[0])-1):
            if grid[i][j] == 5 and isMagic(i, j):
                ans += 1
    return ans


grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
print(numMagicSquaresInside(grid))