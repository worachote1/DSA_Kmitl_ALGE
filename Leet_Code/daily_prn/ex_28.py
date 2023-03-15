class Solution(object):
    def strStr(self, haystack, needle):
        n_haystack,n_needle,Idx_needle = len(haystack),len(needle),0
        i = 0
        while(i<n_haystack):
            if(haystack[i]==needle[Idx_needle]):
                Idx_needle += 1
            else:
                i = i - Idx_needle
                Idx_needle = 0
            if(Idx_needle==n_needle):
                return i-Idx_needle+1
            i+=1
        return -1

test = Solution()
print(test.strStr("mississippi","issip"))