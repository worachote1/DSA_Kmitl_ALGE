class Solution(object):
    def islandPerimeter(self, grid):
        cnt_perimeter,n_row,n_col = 0,len(grid),len(grid[0])
        for i in range(n_row):
            for j in range(n_col):
                if(grid[i][j]==0):
                    continue
                k = 4
                # not the top land
                if(i>0):
                    if(grid[i-1][j]==1):
                        k -= 1
                # not the bottom land
                if(i<n_row-1):
                    if(grid[i+1][j]==1):
                        k -= 1
                # not the most left land
                if(j>0):
                    if(grid[i][j-1]==1):
                        k -= 1
                # not the most right land
                if(j<n_col-1):
                    if(grid[i][j+1]==1):
                        k -= 1
                cnt_perimeter += k
        return cnt_perimeter