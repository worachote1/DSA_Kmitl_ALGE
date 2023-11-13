class Solution(object):
    def matrixReshape(self, mat, r, c):
        cur_row,cur_col = len(mat),len(mat[0])
        if(r*c != cur_col * cur_row):
            return mat
        newArr = [[0 for i in range(0,c)] for j in range(0,r)]
        newArrIdx_row,newArrIdx_col,maxCol = 0,0,c
        for i in range(0,cur_row):
            for j in range(0,cur_col):
                newArr[newArrIdx_row][newArrIdx_col] = mat[i][j]        
                newArrIdx_col += 1
                if (newArrIdx_col >= maxCol):
                    newArrIdx_row,newArrIdx_col = newArrIdx_row+1,0
        return newArr; 

test = Solution()
print(test.matrixReshape([[1,2],[3,4]],1,4))
print(test.matrixReshape([[1,2],[3,4]],2,4))