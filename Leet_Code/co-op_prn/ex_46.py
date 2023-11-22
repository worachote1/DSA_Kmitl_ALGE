class Solution(object):
    def permute(self, nums):
        res = []
        if(len(nums)==1):
            return [[nums[0]]]
        for i in range(0,len(nums)):
            firstVal = nums.pop(0)
            permData = self.permute(nums)
            for item in permData:
                item.append(firstVal)
            for item in permData:
                res.append(item)
            nums.append(firstVal)
        return res
            

test = Solution()
print(test.permute([1,2,3]))
print(test.permute([0,1]))
print(test.permute([1]))