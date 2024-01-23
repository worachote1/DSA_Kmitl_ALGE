class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        for i in range(len(intervals)):
            if(intervals[i][1] < newInterval[0]):
                res.append(intervals[i])
            elif(intervals[i][0] > newInterval[1]):
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval[0] = min(intervals[i][0],newInterval[0])
                newInterval[1] = max(intervals[i][1],newInterval[1])
        return res + [newInterval]

test = Solution() 
print(test.insert([[1,3],[6,9]],[2,5]))
print(test.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
# err case
print(test.insert([[1,5]],[6,8]))