class Solution(object):
    def longestPalindrome(self, s):
        data ={}
        isFoundOdd = False
        res = 0
        for item in s:
            data[item] = data.get(item,0) + 1
        for item in list(data.values()):
            if(item % 2 != 0):
                isFoundOdd = True
                if(item > 1):
                    res += item - 1
            else:
                res += item
        
        if(isFoundOdd):
            return res + 1
        return res

test = Solution()
print(test.longestPalindrome("abccccdd"))
print(test.longestPalindrome("a"))
#err case
print(test.longestPalindrome("ccc"))
        