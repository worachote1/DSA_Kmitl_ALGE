class Solution:
    def longestCommonPrefix(self, strs: list[str]) :
        Lp,Rp,n,res = 0,1,len(strs),200
        while(Rp<n):
            Idx = 0
            cnt = 0
            while(Idx < len(strs[Lp]) and Idx < len(strs[Rp])):
                if(strs[Lp][Idx]==strs[Rp][Idx]):
                    #print("prn =>> "+ strs[Lp][Idx])
                    Idx+=1
                    cnt += 1
                else:
                    break
            res = min(cnt,res)
            Lp = Rp
            Rp+=1
        
        return strs[0][:res] if res != 0 else ""

test = Solution()
print(test.longestCommonPrefix(["flower","flow","flight"]))
print(test.longestCommonPrefix(["dog","racecar","car"]))

#error
print(test.longestCommonPrefix(["ab", "a"]))