class Solution(object):
    def letterCasePermutation(self, s):
        res = []
        def dfs(Idx,cur_ss):
            if(Idx>=len(s)):
                res.append(cur_ss)
                return
            if(ord(s[Idx])>=48 and ord(s[Idx])<=57):
                cur_ss = cur_ss + s[Idx]
                dfs(Idx+1,cur_ss)
            else:
                ss_lower,ss_upper = s[Idx].lower(),s[Idx].upper()
                cur_ss = cur_ss + ss_lower
                dfs(Idx+1,cur_ss)
                cur_ss = cur_ss[:-1]
                cur_ss = cur_ss + ss_upper
                dfs(Idx+1,cur_ss)
        dfs(0,"")
        return res
    
test = Solution()
print(test.letterCasePermutation("a1b2"))
print(test.letterCasePermutation("3z4"))