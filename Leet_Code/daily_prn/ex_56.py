class Solution:
    def merge(self, intervals: List[List[int]]):
        # for i in range(len(intervals)-1):
        #     for j in range(len(intervals)-i-1):
        #         if(intervals[j][0]>intervals[j+1][0]):
        #             intervals[j],intervals[j+1]=intervals[j+1],intervals[j]
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]
        for item in intervals[1:]:
            start,end=item[0],item[1]
            last = res[-1][1]
            if(start<=last):
                res[-1][1]=max(end,last)
            else:
                res.append(item)
        return res