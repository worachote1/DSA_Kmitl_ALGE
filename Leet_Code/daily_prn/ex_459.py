class Solution(object):
    def repeatedSubstringPattern(self, s):
        Idx,n,new_ss = 0,len(s),""
        while(Idx<n//2):
            new_ss += s[Idx]
            k = len(new_ss)
            if(n%k==0):
                if(new_ss*(n//k)==s):
                    return True
            Idx += 1
        return False
    
test = Solution()
print(test.repeatedSubstringPattern("abab"))
print(test.repeatedSubstringPattern("aba"))
print(test.repeatedSubstringPattern("abcabcabcabc"))