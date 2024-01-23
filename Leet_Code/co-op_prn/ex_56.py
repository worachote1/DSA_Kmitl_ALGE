class Solution(object):
    def merge(self, intervals):
        sorted_intervals = sorted(intervals,key=lambda item:item[0])

        res = [sorted_intervals[0]]
        for i in range(1,len(sorted_intervals)):
            if(sorted_intervals[i][0] > res[-1][1]):
                res.append(sorted_intervals[i])
            else:
                startIdx = min(res[-1][0],sorted_intervals[i][0]) 
                endIdx = max(res[-1][1],sorted_intervals[i][1])
                res[-1] = [startIdx,endIdx]

        return res

test = Solution()
print(test.merge([[1,3],[2,6],[8,10],[15,18]]))
print(test.merge([[1,4],[4,5]]))
# err case
print(test.merge([[1,4],[0,4]]))
print(test.merge([[1,4],[2,3]]))
print(test.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))