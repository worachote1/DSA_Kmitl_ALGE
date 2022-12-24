class Solution:
    def longestCommonPrefix(self, strs: list[str]) :
        res = ""
        for i in range(len(strs[0])):
            for item in strs[1:] :
                if(i>=len(item)):
                    return res
                if(item[i]!=strs[0][i]):
                    return res
            res += strs[0][i]
        return res
        
test = Solution()
print(test.longestCommonPrefix(["flower","flow","flight"]))
print(test.longestCommonPrefix(["dog","racecar","car"]))

#error
print(test.longestCommonPrefix(["ab", "a"]))