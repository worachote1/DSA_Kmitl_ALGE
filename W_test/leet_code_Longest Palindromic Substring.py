class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # use: 6 min
        if(len(s) == 1):
            return s

        res_max_pal = s[0]
        for i in range(len(s)):
            # check for odd len pal
            pL = i-1
            pR = i+1
            while(pL>=0 and pR <= len(s)-1):
                if(s[pL] != s[pR]):
                    break
                if(len(s[pL:pR+1]) > len(res_max_pal)):
                    res_max_pal = s[pL:pR+1]
                pL -= 1
                pR += 1

            # check for even len pal
            pL = i
            pR = i+1
            while(pL>=0 and pR <= len(s)-1):
                if(s[pL] != s[pR]):
                    break
                if(len(s[pL:pR+1]) > len(res_max_pal)):
                    res_max_pal = s[pL:pR+1]
                pL -= 1
                pR += 1

        return res_max_pal