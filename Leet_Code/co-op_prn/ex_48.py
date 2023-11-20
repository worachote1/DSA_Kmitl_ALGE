class Solution(object):
    def rotate(self, matrix):
        pLeft,pRight = 0,len(matrix[0])-1
        pTop,pBot = 0,len(matrix)-1
        while(pLeft < pRight):
            n = pRight-pLeft
            for i in range(0,n):
                temp1 = matrix[pTop+i][pRight]
                # change cur top-right -> top-left
                matrix[pTop+i][pRight] = matrix[pTop][pLeft+i]
                # change cur bot-right -> top-right
                temp2 = matrix[pBot][pRight-i]
                matrix[pBot][pRight-i] = temp1
                # change cur bot-left -> bot-right
                temp3 = matrix[pBot-i][pLeft]
                matrix[pBot-i][pLeft] = temp2
                # change cur top-left -> bot-left
                matrix[pTop][pLeft+i] = temp3
            # update val
            pLeft,pRight = pLeft+1,pRight-1
            pTop,pBot = pTop+1,pBot-1
        # print(matrix)
test = Solution()
print(test.rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(test.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))