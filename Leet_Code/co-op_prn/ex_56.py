class Solution(object):
    def merge(self, intervals):
          
    
test = Solution()
print(test.merge([[1,3],[2,6],[8,10],[15,18]]))
print(test.merge([[1,4],[4,5]]))
# err case
print(test.merge([[1,4],[0,4]]))
print(test.merge([[1,4],[2,3]]))
print(test.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))