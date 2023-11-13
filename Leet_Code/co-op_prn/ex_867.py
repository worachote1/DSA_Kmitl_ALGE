class Solution(object):
    def transpose(self, matrix):
        resArr = [];
        for j in range(0,len(matrix[0])):
            newArr = []
            for i in range(0,len(matrix)):
                newArr.append(matrix[i][j])
            resArr.append(newArr)
        return resArr

test = Solution()
print(test.transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(test.transpose([[1,2,3],[4,5,6]]))