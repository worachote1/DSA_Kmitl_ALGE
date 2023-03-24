class PrefixTree():
    def __init__(self) :
        self.children = {}
        self.isLastofWord = False
    def add_word(self,word):
        cur = self
        for item in word:
            if(item not in cur.children):
                cur.children[item] = PrefixTree()
            cur = cur.children[item]
        cur.isLastofWord = True
        # print(list(cur.children))
class Solution(object):
    def findWords(self, board, words):
        root,n_row,n_col,res = PrefixTree(),len(board),len(board[0]),set()
        visited = [[False for j in range(n_col)] for i in range(n_row)]
        for item in words:
            root.add_word(item)
        
        def dfs(Idx_row,Idx_col,cur_Node : PrefixTree,ss):
            if(Idx_row < 0 or Idx_row > n_row-1 or Idx_col < 0 or Idx_col > n_col-1):
                return
            if(board[Idx_row][Idx_col] not in cur_Node.children):
                return
            if(visited[Idx_row][Idx_col]):
                return
            ss += board[Idx_row][Idx_col]
            cur_Node = cur_Node.children[board[Idx_row][Idx_col]]
            if(cur_Node.isLastofWord):
                res.add(ss)
            
            visited[Idx_row][Idx_col] = True
            top_dfs = dfs(Idx_row-1,Idx_col,cur_Node,ss)
            bot_dfs = dfs(Idx_row+1,Idx_col,cur_Node,ss)
            left_dfs = dfs(Idx_row,Idx_col-1,cur_Node,ss)
            right_dfs = dfs(Idx_row,Idx_col+1,cur_Node,ss)
            visited[Idx_row][Idx_col] = False
        
        for i in range(n_row):
            for j in range(n_col):
                dfs(i,j,root,"")
            
        return list(res)

test = Solution()
print(test.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]))
# print(test.findWords([["a","b"],["c","d"]],["abcb"]))
# err
# print(test.findWords([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]],["oa","oaa"]))