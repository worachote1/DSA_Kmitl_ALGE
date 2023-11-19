class Solution(object):
    def generate(self, numRows):
        res = [[1]]
        for i in range(0,numRows-1):
            temp = [0] + res[-1] + [0]
            row_arr = []
            pL,pR = 0,1
            while(pR < len(temp)):
                row_arr.append(temp[pL]+temp[pR])
                pL,pR = pL + 1, pR + 1
            res.append(row_arr)
        return res


test = Solution()
print(test.generate(5))
print(test.generate(1))