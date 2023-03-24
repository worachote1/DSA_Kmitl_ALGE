class Solution(object):
    def findWords(self, board, words):
        n_row,n_col = len(board),len(board[0])
        res,visited = [],[[False for item in range(n_col)] for item in range(n_row)]
        def dfs(Idx_row,Idx_col,Idx_word,word):
            if(Idx_word==len(word)):
                return True
            if(Idx_row < 0 or Idx_row > n_row-1 or Idx_col < 0 or Idx_col > n_col-1):
                return False
            if(visited[Idx_row][Idx_col]):
                return False
            if(board[Idx_row][Idx_col]!=word[Idx_word]):
                return False
        
            visited[Idx_row][Idx_col] = True
            top_dfs = dfs(Idx_row-1,Idx_col,Idx_word+1,word)  
            bot_dfs = dfs(Idx_row+1,Idx_col,Idx_word+1,word)
            left_dfs = dfs(Idx_row,Idx_col-1,Idx_word+1,word)
            right_dfs = dfs(Idx_row,Idx_col+1,Idx_word+1,word)
            if(top_dfs or bot_dfs or left_dfs or right_dfs):
                visited[Idx_row][Idx_col] = False
                return True
            visited[Idx_row][Idx_col] = False
            return False
        
        for item in words:
            check_found = False
            for i in range(n_row):
                for j in range(n_col):
                    if(board[i][j]==item[0] and dfs(i,j,0,item)):
                        res.append(item)
                        check_found = True
                        break
                if(check_found):
                    break
        return res
        
test = Solution()
# print(test.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]))
# print(test.findWords([["a","b"],["c","d"]],["abcb"]))
# err
print(test.findWords([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]],["oa","oaa"]))