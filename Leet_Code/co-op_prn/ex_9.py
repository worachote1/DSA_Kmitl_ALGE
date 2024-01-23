class Solution(object):
    def isPalindrome(self, x):
        if (x < 0):
            return False
        return self.helper(x)
    
    def helper(self,num):
        div_cnt = 0
        temp_num = num
        while(not (temp_num < 10)):
            temp_num /= 10
            div_cnt += 1
        while (num != 0):
            left_digit = num % 10
            right_digit = num // 10**div_cnt
            if(left_digit != right_digit):
                return False
            num = (num % 10**div_cnt) // 10
            div_cnt -= 2
        return True
        
test = Solution()
# print(test.isPalindrome(121))
# print(test.isPalindrome(-121))
# print(test.isPalindrome(10))
# print(test.isPalindrome(9))
# err case
print(test.isPalindrome(1000021))
