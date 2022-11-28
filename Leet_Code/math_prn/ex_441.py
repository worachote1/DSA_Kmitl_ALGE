class Solution:
    def arrangeCoins(self, n: int) :
        l = 0
        r = n
        res = 0
        while(l<=r):
            m = (l+r)//2
            coint_Atrow = (m*(m+1))/2
            if coint_Atrow>n:
                r = m-1
            elif(coint_Atrow<n):
                res = max(m,res)
                l = m+1
            else:
                return m
        return res
test = Solution()
print(test.arrangeCoins(8))
print(test.arrangeCoins(5))
print(test.arrangeCoins(1))
print(test.arrangeCoins(3))