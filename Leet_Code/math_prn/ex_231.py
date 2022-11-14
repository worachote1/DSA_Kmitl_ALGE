class Solution:
    def isPowerOfTwo(self, n: int) :
        if(n==0):
            return False
        return n==1 or (n%2==0 and self.isPowerOfTwo(n//2))
        