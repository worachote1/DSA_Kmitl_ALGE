class Solution:
    def isHappy(self, n: int) :
        data = []
        while(n!=1):
            sumNum = 0
            while(n!=0):
                sumNum += pow(n%10,2)
                n = n//10
            if(sumNum in data):
                return False
            data.append(sumNum)
            n = sumNum

        return True

test = Solution()
print(test.isHappy(19))
print(test.isHappy(2))
#print(test.isHappy(1))
# error
print(test.isHappy(7))