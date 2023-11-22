class Solution(object):
    def countPrimes(self, n):
        checkPrimeArr = [True for i in range(0,n)]
        cnt = 0
        i = 2
        while(i*i < n):
            if(checkPrimeArr[i]):
                j = 2
                while(j*i < n):
                    checkPrimeArr[j*i] = False
                    j += 1
            i += 1

        for i in range(2,len(checkPrimeArr)):
            if(checkPrimeArr[i]):
                cnt+=1        
        return cnt

test = Solution()
# print(test.countPrimes(2))
# print(test.countPrimes(3))
print(test.countPrimes(10))
# print(test.countPrimes(0))
# print(test.countPrimes(1))
# # # err case (Time Limit Exceeded)
# print(test.countPrimes(499979))
# print(test.countPrimes(461465))
print(test.countPrimes(1000000))
