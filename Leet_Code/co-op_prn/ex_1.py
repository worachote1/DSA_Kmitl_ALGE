class Solution(object):
    def twoSum(self, nums, target):
        data = {}
        for i in range(len(nums)):
            find_val = target - nums[i]
            if(find_val not in list(data.keys())):
                data[nums[i]] = i
            else:
                return [data[find_val],i]

test = Solution()
print(test.twoSum([2,7,11,15],9))
print(test.twoSum([3,2,4],6))
print(test.twoSum([3,3],6))