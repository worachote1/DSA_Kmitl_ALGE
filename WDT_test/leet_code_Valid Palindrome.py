class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # use:
        pL = 0
        pR = len(s) - 1
        res = True
        while(pL <= pR):
            if(s[pL].isalnum() and s[pR].isalnum()):
                if(s[pL].lower() == s[pR].lower()):
                    pL += 1
                    pR -= 1
                else:
                    return False
            if(not s[pL].isalnum()):
                pL += 1
            if(not s[pR].isalnum()):
                pR -= 1
        return res