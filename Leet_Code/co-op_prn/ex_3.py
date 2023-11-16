class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res = 0
        pL = 0
        data_set = set()
        s_len = len(s)
        for i in range(0,s_len):
            while(s[i] in data_set):
                data_set.remove(s[pL])
                pL += 1
            if(i - pL + 1 > res):
                res = i - pL + 1 
            data_set.add(s[i])
        return res
    
test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))
print(test.lengthOfLongestSubstring("bbbbb"))
print(test.lengthOfLongestSubstring("pwwkew"))