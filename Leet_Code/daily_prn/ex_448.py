class Solution(object):
    def findDisappearedNumbers(self, nums):
        return list(set([i for i in range(1,len(nums)+1)]) - set(nums))

test = Solution()

        