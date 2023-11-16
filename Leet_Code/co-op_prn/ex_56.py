class Solution(object):
    def merge(self, intervals):
        res = []
        i = 0
        sort_intervals = sorted(intervals,key=lambda item :item[0])
        len_intervals = len(sort_intervals)
        while(i < len_intervals):
            pL,pR = sort_intervals[i][0],sort_intervals[i][1]
            while(i < len_intervals - 1):
                if(pR >= sort_intervals[i+1][1]):
                    i += 1
                    continue
                if(pR >= sort_intervals[i+1][0]):
                    pR = sort_intervals[i+1][1]
                    i += 1
                else:
                    break
            i += 1
            res.append([pL,pR])
        return res
    
test = Solution()
print(test.merge([[1,3],[2,6],[8,10],[15,18]]))
print(test.merge([[1,4],[4,5]]))
#err case
print(test.merge([[1,4],[0,4]]))
print(test.merge([[1,4],[2,3]]))
print(test.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))