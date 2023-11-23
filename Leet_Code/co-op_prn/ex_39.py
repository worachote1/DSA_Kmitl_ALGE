class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def dfs(Idx,curArr,curTarget):
            if(curTarget == target):
                res.append([item for item in curArr])
                return 
            if(curTarget > target):
                return
            if(Idx >= len(candidates)):
                return
            
            dfs(Idx,curArr+[candidates[Idx]],curTarget+candidates[Idx])
            dfs(Idx+1,curArr,curTarget)
        dfs(0,[],0)
        return res
    
test = Solution()
print(test.combinationSum([2,3,6,7],7))
print(test.combinationSum([2,3,5],8))
print(test.combinationSum([2],1))