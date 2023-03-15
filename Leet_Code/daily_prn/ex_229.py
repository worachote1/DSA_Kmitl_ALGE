# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Follow up: Could you solve the problem in linear time and in O(1) space?
class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        n, cnt, res = len(nums), 1, []
        if(n < 3):
            return list(set(nums))
        for i in range(n-1):
            if(nums[i] == nums[i+1]):
                cnt += 1
                if(cnt > n//3):
                    res.append(nums[i])
            else:
                cnt = 1
        return list(set(res))
    
test = Solution()
print(test.majorityElement([3,2,3]))
print(test.majorityElement([1]))
print(test.majorityElement([1,2]))
print(test.majorityElement([2,2]))