class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) :
        res = []
        for i in range(len(intervals)):
            #come before
            if(newInterval[1]<intervals[i][0]):
                res.append(newInterval)
                return res + intervals[i:]
            #come after
            elif(newInterval[0]>intervals[i][1]):
                res.append(intervals[i])
            #overlap
            else:
                newInterval[0],newInterval[1]=min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])
        return res+[newInterval]

test = Solution()
print(test.insert([[1,3],[6,9]],[2,5]))