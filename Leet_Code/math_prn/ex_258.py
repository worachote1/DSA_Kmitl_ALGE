#"The original number is divisible by 9 if and only if the sum of its digits is divisible by 9"
# find digit root
# n = d0 + d1*10 + d2*100 + d3*1000
# n = d0 + d1*(9+1) + d2*(99+1) + d3(999+1)
# n = d0 + d1*(9+1) + d2*((9*11)+1) + d3((9*111)+1)
# n = d0 + 9*d1 + d1 + 9*(11*d2) + d2 + 9*(111*d3) + d3
# n = d0 + d1 + d2 + d3 + 9(d1 + 11*d2 + 111*d3)
# n % 9 = (d0 + d2 + d2 ) % 9
class Solution:
    def addDigits(self, num: int) :
        if(num==0):
            return 0
        if(num % 9 == 0):
            return 9
        return num % 9

test = Solution()
print(test.addDigits(18))


        