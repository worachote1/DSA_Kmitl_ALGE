class Solution(object):
    def strStr(self, haystack, needle):
        step = len(needle)
        end = len(haystack)
        for i in range(0,end):
            if(i+step > end):
                break
            if(needle==haystack[i:i+step]):
                return i
        return -1
