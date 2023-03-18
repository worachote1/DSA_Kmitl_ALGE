class Solution(object):
    def transpose(self, matrix):
        n_row,n_col,new_IdxRow,new_IdxCol = len(matrix),len(matrix[0]),0,0
        res = [[0 for j in range(n_row)] for i in range(n_col)]
        for i in range(n_col):
            for j in range(n_row):
                new_IdxRow,new_IdxCol = i,j
                res[new_IdxRow][new_IdxCol] = matrix[j][i]
        return res
test = Solution()
print(test.transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(test.transpose([[1,2,3],[4,5,6]]))