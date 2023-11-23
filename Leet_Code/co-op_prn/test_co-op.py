class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        curSubset = []
        nums.sort()
        def dfs(Idx):
            if(Idx >= len(nums)):
                res.append([item for item in curSubset])
                return
            curSubset.append(nums[Idx])
            # print("prn1 -> ",curSubset)
            dfs(Idx+1)
            curSubset.pop()
            # print("prn2 -> ",curSubset)
            while(Idx < len(nums)-1 and nums[Idx] == nums[Idx+1]):
                Idx += 1
            dfs(Idx+1)
        dfs(0)
        return res

test = Solution()
print(test.subsetsWithDup([1,2,2]))
print(test.subsetsWithDup([0]))
#err case
print(test.subsetsWithDup([4,4,4,1,4]))
