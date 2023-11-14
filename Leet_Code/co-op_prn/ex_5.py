class Solution(object):
    def longestPalindrome(self, s):
        res = s[0]
        for i in range(0,len(s)):
            # check odd-palindrome
            pL,pR = i-1, i+1
            while(pL >= 0 and pR <= len(s) - 1):
                if(s[pL] != s[pR]):
                    break
                if(pR - pL + 1 > len(res)):
                    res = s[pL:pR+1]
                pL -= 1
                pR += 1
            # check even-palindrome
            pL,pR = i, i+1
            while(pL >= 0 and pR <= len(s) - 1):
                if(s[pL] != s[pR]):
                    break
                if(pR - pL + 1> len(res)):
                    res = s[pL:pR+1]
                pL -= 1
                pR += 1
        return res

test = Solution()
print(test.longestPalindrome("babad"))
print(test.longestPalindrome("cbbd"))