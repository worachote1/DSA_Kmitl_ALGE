class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]):
        res,row,col = [],len(matrix),len(matrix[0])
        for i in range(col):
            if(not self.helper(matrix,0,i)):
                return False
        for i in range(1,row):
            if(not self.helper(matrix,i,0)):
                return False
        return True
            
    def helper(self,matrix : list,row : int,col : int):
        val = matrix[row][col]
        while(row<len(matrix) and col<len(matrix[0])):
            if(val != matrix[row][col]):
                return False
            row,col=row+1,col+1
        return True
test = Solution()
print(test.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(test.isToeplitzMatrix([[1,2],[2,2]]))