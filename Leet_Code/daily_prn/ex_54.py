class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        start_row,end_row,start_col,end_col = 0,len(matrix)-1,0,len(matrix[0])-1
        while(start_row <= end_row and start_col <= end_col):
            for i in range(start_col,end_col+1):
                res.append(matrix[start_row][i])
            start_row += 1
            if(start_row > end_row):
                break

            for i in range(start_row,end_row+1):
                res.append(matrix[i][end_col])
            end_col -= 1
            if(start_col > end_col):
                break               
            
            for i in range(end_col,start_col-1,-1):
                res.append(matrix[end_row][i])
            end_row -= 1
            
            for i in range(end_row,start_row-1,-1):
                res.append(matrix[i][start_col])
            start_col += 1
            
        return res
    
test = Solution()
print(test.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(test.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))