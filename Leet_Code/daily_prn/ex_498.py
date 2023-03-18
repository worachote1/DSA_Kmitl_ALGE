# 498. Diagonal Traverse
class Solution(object):
    def findDiagonalOrder(self, mat):
        res,isUp,Idx_row,Idx_col,n_row,n_col = [],True,0,0,len(mat),len(mat[0])
        end = n_row * n_col
        while(len(res)<end):
            if(isUp):
                while(True):
                    res.append(mat[Idx_row][Idx_col])
                    Idx_row,Idx_col = Idx_row-1,Idx_col+1
                    if(Idx_col > n_col-1):
                        Idx_row,Idx_col,isUp = Idx_row+2,Idx_col-1,False
                        break
                    elif(Idx_row < 0):
                        Idx_row,isUp = Idx_row+1,False
                        break
            else:
                while(True):
                    res.append(mat[Idx_row][Idx_col])
                    Idx_row,Idx_col = Idx_row+1,Idx_col-1
                    if(Idx_row > n_row-1):
                        Idx_col,Idx_row,isUp = Idx_col+2,Idx_row-1,True
                        break
                    elif(Idx_col < 0):
                        Idx_col,isUp = Idx_col+1,True
                        break
        return res

test = Solution()
print(test.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(test.findDiagonalOrder([[1,2],[3,4]]))
        