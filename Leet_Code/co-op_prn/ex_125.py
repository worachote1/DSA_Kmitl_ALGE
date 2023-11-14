class Solution(object):
    def isPalindrome(self, s):
        return self.check_valid_palindrome(s,0,len(s)-1)
    
    def check_valid_palindrome(self, ss, pL, pR):
        if (pL >= pR):
            return True
        while(not ss[pL].isalnum() or not ss[pR].isalnum()):
            if(not ss[pL].isalnum()):
                pL += 1
            if(not ss[pR].isalnum()):
                pR -= 1
            if (pL >= pR):
                return True
        if (ss[pL].lower() != ss[pR].lower()):
            return False
        return self.check_valid_palindrome(ss,pL+1,pR-1)

test = Solution()
print(test.isPalindrome("A man, a plan, a canal: Panama"))
print(test.isPalindrome("race a car"))
print(test.isPalindrome(" "))
print(test.isPalindrome("0P"))