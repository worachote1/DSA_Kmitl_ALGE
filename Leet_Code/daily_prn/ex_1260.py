class Solution(object):
    def shiftGrid(self, grid, k):
        n_row,n_col = len(grid),len(grid[0])
        for i in range(k):
            temp = grid[0][0]
            for j in range(0,n_row):
                for k in range(1,n_col):
                    temp_2 = grid[j][k]
                    grid[j][k] = temp 
                    temp = temp_2
                if(j<n_row-1):
                    temp2 = grid[j+1][0]
                    grid[j+1][0] = temp
                    temp = temp2
            grid[0][0]=temp
        return grid
    
test = Solution()
print(test.shiftGrid([[1,2,3],[4,5,6],[7,8,9]],1))
print(test.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]],4))
print(test.shiftGrid([[1,2,3],[4,5,6],[7,8,9]],9))