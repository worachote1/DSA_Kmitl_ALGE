class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # use: 1 min
        pL = 0
        pR = len(s)-1
        while(pL <= pR):
            temp = s[pR]
            s[pR] = s[pL]
            s[pL] = temp
            pL += 1
            pR -= 1