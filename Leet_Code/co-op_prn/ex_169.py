class Solution(object):
    def majorityElement(self, nums):
        data = {}
        len_nums = len(nums)
        for item in nums:
            data[item] = data.get(item,0) + 1
            if(data[item] > len_nums / 2):
                return item
        
test = Solution()
print(test.majorityElement([3,2,3]))
print(test.majorityElement([2,2,1,1,1,2,2]))