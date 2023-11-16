class Solution(object):
    def exist(self, board, word):
        visited_path = set()
        def dfs(p_word,pRow,pCol):
            if(p_word == len(word)):
                return True
            if(pRow < 0 or pRow > len(board) - 1
               or pCol < 0 or pCol > len(board[0]) - 1):
                return False
            # print("pRow -> {0} | pCol -> {1} | p_word -> {2} | cur_board -> {3}".format(pRow,pCol,p_word,board[pRow][pCol]))
            if(board[pRow][pCol] != word[p_word]):
                return False
            if((pRow,pCol) in visited_path):
                return False
            visited_path.add((pRow,pCol))
            find_top = dfs(p_word + 1,pRow - 1,pCol)
            find_bot = dfs(p_word + 1,pRow + 1,pCol)
            find_left = dfs(p_word + 1,pRow,pCol - 1)
            find_right = dfs(p_word + 1,pRow,pCol + 1)
            visited_path.remove((pRow,pCol))
            return find_top or find_bot or find_left or find_right
        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if(board[i][j] != word[0]):
                    continue
                if(dfs(0,i,j)):
                    return True
        return False
        
test = Solution()
# print(test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCV"))
print(test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
print(test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
print(test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))
    