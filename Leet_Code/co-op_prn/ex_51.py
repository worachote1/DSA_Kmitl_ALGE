class Solution(object):
    def solveNQueens(self, n):
        res = []
        board = [["."]*n for i in range(n)]
        colData = set()
        negDiaData = set()
        posDiaData = set()
        def helper(curRow):
            if(curRow == n):
                res.append(["".join(item) for item in board])
                return
            for col in range(n):
                if(col in colData):
                    continue
                elif(col - curRow in negDiaData):
                    continue
                elif(col + curRow in posDiaData):
                    continue
                board[curRow][col] = "Q"
                colData.add(col)
                negDiaData.add(col - curRow)
                posDiaData.add(col + curRow)
                helper(curRow+1)
                board[curRow][col] = "."
                colData.remove(col)
                negDiaData.remove(col - curRow)
                posDiaData.remove(col + curRow)      

        helper(0)
        return res

test = Solution()
print(test.solveNQueens(4))
print(test.solveNQueens(1))