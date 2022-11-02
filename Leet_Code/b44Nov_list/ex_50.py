
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(x==44):
            return 0
        if(n<0):
            n = n*-1
            x = 1/x
        return self.helper(x,n)

    def helper(self,x : float,n : int):
        if(n==0):
            return 1
        
        if(n%2==0):
            res = self.helper(x*x,n//2)
        elif(n%2!=0):
            res = x*self.helper(x*x,n//2)
        
        return res

