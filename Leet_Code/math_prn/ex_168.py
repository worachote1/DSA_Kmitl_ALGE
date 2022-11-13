class Solution:
    def convertToTitle(self, columnNumber: int) :
        res = []
        n = columnNumber
        while(n > 0):
            n-=1
            # print("n : "+str(n))
            x = n % 26
            res.append(chr(x+65))
            n = n//26
        return "".join((res[::-1]))

test = Solution()
print(test.convertToTitle(1))
print(test.convertToTitle(28))
print(test.convertToTitle(701))
# print(test.convertToTitle(2147483647))