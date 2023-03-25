class PrefixTree():
    def __init__(self) :
        self.children = {}
        self.isEndOfWord = False
    
    def add_word(self,word):
        cur = self
        for item in word:
            if(item not in cur.children):
                cur.children[item] = PrefixTree()
            cur =cur.children[item]
        cur.isEndOfWord = True
    
    def remove_word(self,word,Idx,cur):
        if(Idx==len(word)):
            if(not cur.isEndOfWord):
                return False
            cur.isEndOfWord = False
            return len(cur.children)==0
        char = word[Idx]
        if(char not in cur.children):
            return False
        next_Node = cur.children[char]
        able_to_remove = self.remove_word(word,Idx+1,next_Node)
        if(able_to_remove):
            del next_Node
            return len(cur)==0
        return False

class Solution(object):
    def findWords(self, board, words):
        res,n_row,n_col = [],len(board),len(board[0])
        visited = [[False for j in range(n_col)] for i in range(n_row)]
        root = PrefixTree()
        for item in words:
            root.add_word(item)
        
        def dfs(Idx_row,Idx_col,cur_Node,ss_word):
            if(Idx_row < 0 or Idx_row > n_row-1 or Idx_col < 0 or Idx_col > n_col-1):
                return False
            if(board[Idx_row][Idx_col] not in cur_Node.children):
                return False
            if(visited[Idx_row][Idx_col]):
                return False
            ss_word += board[Idx_row][Idx_col]
            visited[Idx_row][Idx_col] = True
            cur_Node = cur_Node.children[board[Idx_row][Idx_col]]
            if(cur_Node.isEndOfWord):
                res.append(ss_word)
                root.remove_word(ss_word)
            top_dfs = dfs(Idx_row-1,Idx_col,cur_Node,ss_word)
            bot_dfs = dfs(Idx_row+1,Idx_col,cur_Node,ss_word)
            left_dfs = dfs(Idx_row,Idx_col-1,cur_Node,ss_word)
            right_dfs = dfs(Idx_row,Idx_col+1,cur_Node,ss_word)
            visited[Idx_row][Idx_col] = False

        for i in range(n_row):
            for j in range(n_col):
                dfs(i,j,root,"")
        return res

test = Solution()
print(test.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]))
# print(test.findWords([["a","b"],["c","d"]],["abcb"]))
# err
# print(test.findWords([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]],["oa","oaa"]))