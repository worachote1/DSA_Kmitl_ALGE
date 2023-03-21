class Solution(object):
    def tictactoe(self, moves):
        grid,isPending = [["" for j in range(3)] for i in range(3)],False
        def create_grid():
            cnt_Idx = 0
            cnt_check_pending = len(grid) * len(grid[0])
            for item in moves:
                grid[item[0]][item[1]],cnt_Idx,cnt_check_pending = "x" if cnt_Idx % 2 == 0 else "o",cnt_Idx+1,cnt_check_pending-1
            return True if cnt_check_pending!=0 else False
        def check_row():
            return "A" if grid[0][0]==grid[0][1]==grid[0][2]=="x" or grid[1][0]==grid[1][1]==grid[1][2]=="x" or grid[2][0]==grid[2][1]==grid[2][2]=="x" else "B" if grid[0][0]==grid[0][1]==grid[0][2]=="o" or grid[1][0]==grid[1][1]==grid[1][2]=="o" or grid[2][0]==grid[2][1]==grid[2][2]=="o" else None
        def check_col():
            return "A" if grid[0][0]==grid[1][0]==grid[2][0]=="x" or grid[0][1]==grid[1][1]==grid[2][1]=="x" or grid[0][2]==grid[1][2]==grid[2][2]=="x" else "B" if grid[0][0]==grid[1][0]==grid[2][0]=="o" or grid[0][1]==grid[1][1]==grid[2][1]=="o" or grid[0][2]==grid[1][2]==grid[2][2]=="o" else None
        def check_diagonal():
            return "A" if grid[0][0]==grid[1][1]==grid[2][2]=="x" else "B" if grid[0][0]==grid[1][1]==grid[2][2]=="o" else None
        def check_reversed_diagonal():
            return "A" if grid[0][2]==grid[1][1]==grid[2][0]=="x" else "B" if grid[0][2]==grid[1][1]==grid[2][0]=="o" else None
        
        isPending = create_grid()
        return check_row() if check_row() != None else check_col() if check_col() != None else check_diagonal() if check_diagonal() != None else check_reversed_diagonal() if check_reversed_diagonal() != None else "Pending" if isPending else "Draw"
        

test = Solution()
print(test.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
print(test.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
print(test.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))