#Ex 409 Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        return self.helper(s)

    def helper(self, s : str) ->str:
        data = {}
        for item in s :
            if(item not in data):
                data[item] = 1
                continue
            data[item]+=1
        
        res = 0
        for item in data:
            res += data[item]//2*2
            if(data[item] % 2 != 0 and res % 2 == 0):
                res += 1
        
        return res