class Solution(object):
    def findDuplicate(self, nums):
        data = {}
        for item in nums:
            data[item] = data.get(item,0) + 1
            if (data[item] > 1):
                return item

test = Solution()
print(test.findDuplicate([1,3,4,2,2]))
print(test.findDuplicate([3,1,3,4,2]))