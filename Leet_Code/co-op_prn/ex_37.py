class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rowData = {}
        colData = {}
        allGridData = {}
        # create default data
        for i in range(9):
            for j in range(9):
                if(i not in rowData):
                    rowData[i] = set()
                if(j not in colData):
                    colData[j] = set()
                virtualPair = (i//3,j//3)
                if(virtualPair not in allGridData):
                    allGridData[virtualPair] = set()

                if(not board[i][j].isdigit()):
                    continue

                rowData[i].add(board[i][j])

                colData[j].add(board[i][j])

                allGridData[virtualPair].add(board[i][j])                

        def isValidSudoku(row,col,val):
            virtualPair = (row//3,col//3)
            return (val not in rowData[row] and 
                    val not in colData[col] 
                    and
                    val not in allGridData[virtualPair]
                    ) 
        
        def solve(curRow,curCol):
            if(curRow == 9):
                return True
            if(curCol == 9):
                return solve(curRow+1,0)
            # print(board)
            if(board[curRow][curCol].isdigit()):
                return solve(curRow,curCol+1)
            else:
                for i in range(1,10):
                    val = str(i)
                    if(isValidSudoku(curRow,curCol,val)):
                        virtualPair = (curRow//3,curCol//3)
                        board[curRow][curCol] = val
                        rowData[curRow].add(val)
                        colData[curCol].add(val)
                        allGridData[virtualPair].add(val)
                        solveNext = solve(curRow,curCol+1)
                        if(not solveNext):
                            board[curRow][curCol] = "."
                            rowData[curRow].remove(val)
                            colData[curCol].remove(val)
                            allGridData[virtualPair].remove(val)
                        
                        else:
                            return True
                return False
        solve(0,0)
        # print(board)

test = Solution()
# print(test.solveSudoku([
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
#     ]))

# err case

print(test.solveSudoku([
 [".",".","9","7","4","8",".",".","."],
 ["7",".",".",".",".",".",".",".","."],
 [".","2",".","1",".","9",".",".","."],
 [".",".","7",".",".",".","2","4","."],
 [".","6","4",".","1",".","5","9","."],
 [".","9","8",".",".",".","3",".","."],
 [".",".",".","8",".","3",".","2","."],
 [".",".",".",".",".",".",".",".","6"],
 [".",".",".","2","7","5","9",".","."]
]))