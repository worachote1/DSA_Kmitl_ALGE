class Solution(object):
    def exist(self, board, word):
        n_row,n_col = len(board),len(board[0])
        def dfs(Idx_row,Idx_col,prev_Idx,cur_ss):
            if(Idx_row > n_row-1 or Idx_row < 0 or Idx_col < 0 or Idx_col > n_col-1):
                return False
            if([Idx_row,Idx_col] in prev_Idx):
                return False
            cur_ss = cur_ss + board[Idx_row][Idx_col]
            prev_Idx.append([Idx_row,Idx_col])
            if(len(cur_ss)==len(word)):
                return True if cur_ss == word else False
            dfs_next_top,dfs_next_bottom = dfs(Idx_row-1,Idx_col,[item for item in prev_Idx],cur_ss),dfs(Idx_row+1,Idx_col,[item for item in prev_Idx],cur_ss)
            dfs_next_left,dfs_next_right = dfs(Idx_row,Idx_col-1,[item for item in prev_Idx],cur_ss),dfs(Idx_row,Idx_col+1,[item for item in prev_Idx],cur_ss)
            return dfs_next_top or dfs_next_bottom or dfs_next_left or dfs_next_right
               
        for i in range(n_row):
            for j in range(n_col):
                if(not dfs(i,j,[],"")):
                    continue
                return True
        return False

test = Solution()
print(test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
print(test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
print(test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))