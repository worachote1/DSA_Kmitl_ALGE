class Solution(object):
    def isPalindrome(self, x):
        if(x < 0):
            return False
        tempNum = x
        divCnt = 0
        while(tempNum >= 10):
            tempNum /= 10
            divCnt += 1
        while(x != 0):
            leftDigit = x // 10**divCnt
            rightDigit = x % 10
            if(leftDigit != rightDigit):
                return False
            x = (x % 10**divCnt) // 10
            divCnt -= 2

        return True


test = Solution()
print(test.isPalindrome(121))
print(test.isPalindrome(-121))
print(test.isPalindrome(10))
print(test.isPalindrome(9))
# err case
print(test.isPalindrome(1000021))