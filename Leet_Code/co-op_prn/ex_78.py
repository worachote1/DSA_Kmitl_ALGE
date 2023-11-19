class Solution(object):
    def subsets(self, nums):
        res = []
        def helper(curIdx,curArr):
            if(curIdx >= len(nums)):
                res.append(curArr)
                return
            helper(curIdx+1,curArr)
            helper(curIdx+1,curArr + [nums[curIdx]])

        helper(0,[])
        return res

test = Solution()
print(test.subsets([1,2,3]))
print(test.subsets([0]))