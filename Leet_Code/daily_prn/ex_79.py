class Solution(object):
    def exist(self, board, word):
        n_row,n_col = len(board),len(board[0])
        visited_check = [[False for j in range(n_col)] for i in range(n_row)]
        def dfs(Idx_row,Idx_col,cnt):
            if(cnt==len(word)):
                return True
            if(Idx_row > n_row-1 or Idx_row < 0 or Idx_col < 0 or Idx_col > n_col-1):
                return False
            if(visited_check[Idx_row][Idx_col]):
                return False
            if(board[Idx_row][Idx_col]!=word[cnt]):
                return False
            visited_check[Idx_row][Idx_col]=True
            dfs_next_top,dfs_next_bottom = dfs(Idx_row-1,Idx_col,cnt+1),dfs(Idx_row+1,Idx_col,cnt+1)
            dfs_next_left,dfs_next_right = dfs(Idx_row,Idx_col-1,cnt+1),dfs(Idx_row,Idx_col+1,cnt+1)
            if(dfs_next_top or dfs_next_bottom or dfs_next_left or dfs_next_right):
                return True
            visited_check[Idx_row][Idx_col]=False
            return False
        for i in range(n_row):
            for j in range(n_col):
                if(board[i][j]==word[0] and dfs(i,j,0)):
                    return True
        return False

test = Solution()
print(test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
print(test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
print(test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))

# err (Time Limit Exceeded)
print(test.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]],"AAAAAAAAAAAABAA"))