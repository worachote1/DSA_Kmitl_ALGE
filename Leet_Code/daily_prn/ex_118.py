class Solution:
    def generate(self, numRows: int) :
        res = [[1]]
        for i in range(numRows-1):
            m = [0] + res[-1] + [0]
            newArr = []
            for j in range(len(res[-1])+1):
                newArr.append(m[j]+m[j+1])
            res.append(newArr)
        return res

test = Solution()
print(test.generate(5))