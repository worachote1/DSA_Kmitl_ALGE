class Solution(object):
    def surfaceArea(self, grid):
        row,col,res = len(grid),len(grid[0]),0
        for i in range(row):
            for j in range(col):
                if(grid[i][j]==0):
                    continue
                res += (6*grid[i][j]) - (2*(grid[i][j]-1))
                if(j<col-1):
                    res -= 2 * min(grid[i][j],grid[i][j+1])
                if(i>0):
                    res -= 2 * min(grid[i][j],grid[i-1][j])
        return res

test = Solution()
print(test.surfaceArea([[1,2],[3,4]]))
print(test.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
print(test.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))