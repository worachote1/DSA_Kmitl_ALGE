class Solution(object):
    def findDisappearedNumbers(self, nums):
        res,n = [],len(nums)
        for item in nums:
            temp = abs(item)-1
            if(nums[temp]>0):
                nums[temp] *= -1
        for i in range(n):
            if(nums[i]>0):
                res.append(i+1)
        return res
test = Solution()
print(test.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(test.findDisappearedNumbers([1,1]))

        