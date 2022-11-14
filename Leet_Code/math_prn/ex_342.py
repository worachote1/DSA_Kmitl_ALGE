class Solution:
    def isPowerOfFour(self, n: int) :
        return (n!=0) and ((n==1) or n%4==0 and self.isPowerOfFour(n/4))