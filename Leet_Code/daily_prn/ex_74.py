class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) :
        row,col = 0,len(matrix[0])-1
        while(row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])):
            if(matrix[row][col]<target):
                row += 1
            elif(matrix[row][col]>target):
                col -= 1
            if(matrix[row][col]==target):
                return True
        return False