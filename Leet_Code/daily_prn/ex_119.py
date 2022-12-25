class Solution:
    def getRow(self, rowIndex: int) :
        res = [1]
        for i in range(rowIndex):
            m = [0]+res+[0]
            prev = []
            for j in range(len(res)+1):
                prev.append(m[j]+m[j+1])
            res = prev
        return res
test=Solution()
print(test.getRow(0))
print(test.getRow(1))
print(test.getRow(3))
