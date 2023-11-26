class Solution(object):
    def isValidSudoku(self, board):
        digitDataRow = set()
        digitDataCol = set()
        checkAllGridData = {}

        for i in range(len(board)//3):
            for j in range(len(board[0])//3):
                virtualPair = (i,j)
                checkAllGridData[virtualPair] = []
    
        # check by row and check if any grid doesn't have digit
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(not board[i][j].isdigit()):
                    continue
                if(board[i][j] in digitDataRow):
                    return False
                digitDataRow.add(board[i][j])
                
                virtualPair = (i//3,j//3)
                if(board[i][j] in checkAllGridData[virtualPair]):
                    return False
                checkAllGridData[virtualPair].append(board[i][j])
            digitDataRow.clear()

        #check by col
        for i in range(len(board[0])):
            for j in range(len(board)):
                if(not board[j][i].isdigit()):
                    continue
                if(board[j][i] in digitDataCol):
                    return False
                digitDataCol.add(board[j][i])
            digitDataCol.clear()                

        return True

test = Solution()
print(test.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(test.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

#err case
print(test.isValidSudoku(
    [[".",".",".",".","5",".",".","1","."],
     [".","4",".","3",".",".",".",".","."],
     [".",".",".",".",".","3",".",".","1"],
     ["8",".",".",".",".",".",".","2","."],
     [".",".","2",".","7",".",".",".","."],
     [".","1","5",".",".",".",".",".","."],
     [".",".",".",".",".","2",".",".","."],
     [".","2",".","9",".",".",".",".","."],
     [".",".","4",".",".",".",".",".","."]]
))