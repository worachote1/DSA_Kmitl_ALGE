class Solution(object):
    def getRow(self, rowIndex):
        # Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
        res = [1]
        for i in range(rowIndex):
            temp = [0] + res + [0]
            pL,pR = 0,1
            curRow_arr = []
            while(pR < len(temp)):
                val = temp[pL] + temp[pR]
                curRow_arr.append(val)
                pL,pR = pL+1,pR+1
            res = curRow_arr
        return res

test = Solution()
print(test.getRow(3))
print(test.getRow(0))
print(test.getRow(1))