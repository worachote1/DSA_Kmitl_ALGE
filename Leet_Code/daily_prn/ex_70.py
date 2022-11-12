class Solution:
    def climbStairs(self, n : int) :
        return self.helper(n)

    def helper(self, n  : int):
        x = 1
        y = 2
        
        for i in range(3,n+1):
            temp = x
            x = y
            y += temp
        
        return y if n!=1 else 1