class Solution:
    def hasAlternatingBits(self, n: int) :
        while(n != 0):
            last = n%2
            last_2 = (n>>1) % 2
            if(last==last_2):
                return False
            n = n>>1
        return True
    
test = Solution()
print(test.hasAlternatingBits(5))
print(test.hasAlternatingBits(7))
print(test.hasAlternatingBits(11))

            