
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]

class Solution(object):
    def matrixReshape(self, mat, r, c):
        n_row,n_col,new_mat = len(mat),len(mat[0]),[[] for item in range(r)]
        if(n_row * n_col != r*c):
            return mat
        Idx,k = 0,0
        for i in range(n_row):
            for j in range(n_col):
                new_mat[Idx].append(mat[i][j])
                k+=1
                if(k==c):
                    k,Idx=0,Idx+1
        return new_mat
    
test = Solution()
print(test.matrixReshape([[1,2],[3,4]],1,4))
        