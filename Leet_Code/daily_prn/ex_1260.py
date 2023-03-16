class Solution(object):
    def shiftGrid(self, grid, k):
        n_row,n_col = len(grid),len(grid[0])
        temp_arr = [0 for i in range(n_row*n_col)]
        n_temp_arr = len(temp_arr)
        #covert 2D to 1D
        for i in range(n_row):
            for j in range(n_col):
                temp_arr[((i*n_col+j+k)%(n_temp_arr))]=grid[i][j]
        #convert 1D to 2D
        for i in range(n_temp_arr):
            Idx_new_row,Idx_new_col= i//n_col,i%n_col
            grid[Idx_new_row][Idx_new_col] = temp_arr[i]
        return grid
    
test = Solution()
print(test.shiftGrid([[1,2,3],[4,5,6],[7,8,9]],1))
# print(test.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]],4))
# print(test.shiftGrid([[1,2,3],[4,5,6],[7,8,9]],9))
# error test case
print(test.shiftGrid([[1],[2],[3],[4],[7],[6],[5]],23)) # [[6],[5],[1],[2],[3],[4],[7]]
