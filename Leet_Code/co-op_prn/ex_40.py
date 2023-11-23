class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        data = {}
        candidates.sort()
        for item in candidates:
            data[item] = data.get(item,0) + 1
        # print(data)
        def dfs(Idx,curArr,curTarget):
            if(curTarget==target):
                res.append([item for item in curArr])
                return
            if(curTarget > target):
                return
            if(Idx >= len(data)):
                return
            if(data[list(data)[Idx]] > 0):
                curArr.append(list(data)[Idx])
                data[list(data)[Idx]] = data.get(list(data)[Idx]) - 1
                dfs(Idx,curArr,curTarget+list(data)[Idx])
                curArr.pop()
                data[list(data)[Idx]] = data.get(list(data)[Idx]) + 1
            dfs(Idx+1,curArr,curTarget)

        dfs(0,[],0)
        return res
        
test = Solution()
print(test.combinationSum2([10,1,2,7,6,1,5],8))
print(test.combinationSum2([2,5,2,1,2],5))
# err case
print(test.combinationSum2([1,2],4))