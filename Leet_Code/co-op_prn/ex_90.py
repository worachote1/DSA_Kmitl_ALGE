class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        def helper(curIdx,curArr):
            if(curIdx >= len(nums)):
                res.append(curArr)
                return
            helper(curIdx+1,curArr + [nums[curIdx]])
            while(curIdx + 1 < len(nums) and nums[curIdx] == nums[curIdx+1]):
                curIdx += 1
            helper(curIdx+1,curArr)

        helper(0,[])
        return res
test = Solution()
print(test.subsetsWithDup([1,2,2]))
print(test.subsetsWithDup([0]))
        