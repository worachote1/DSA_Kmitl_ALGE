class Solution:
    def restoreIpAddresses(self, s: str) :
        res = []
        if(len(s)>12):
            return []
        self.helper(res,s,0,0,"")
        return res
    def helper(self,res_arr : list,s : str,Idx : int,dot : int,curIP : str):
        if(dot==4 and Idx == len(s)):
            res_arr.append(curIP[:len(curIP)-1])
        if(dot > 4):
            return
        for j in range(Idx,min(Idx+3,len(s))):
            k = int(s[Idx:j+1])
            if(k>255 or k<0):
                return
            if(s[Idx:j+1][0]=="0" and len(s[Idx:j+1])>1):
                return
            self.helper(res_arr,s,j+1,dot+1,curIP+str(k)+".")

test = Solution()
print(test.restoreIpAddresses("25525511135"))
print(test.restoreIpAddresses("0000"))
print(test.restoreIpAddresses("101023"))