class Solution:
    def generateParenthesis(self, n: int) :
        res = []
        self.helper(n,res,"",0,0)
        return res

    def helper(self,n : int,res : list,ss : str,open_count : int,close_count : int):
        if(len(ss)==2*n):
            res.append(ss)
            return
     
        if(open_count<n):
            self.helper(n,res,ss+"(",open_count+1,close_count)
        if(open_count>close_count):
            self.helper(n,res,ss+")",open_count,close_count+1)


test = Solution()
print(test.generateParenthesis(1))