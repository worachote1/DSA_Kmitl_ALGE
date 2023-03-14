class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        data = {}
        for i in range(len(nums)):
            if(nums[i] in data):
                if(i-data[nums[i]]<=k):
                    return True
            data[nums[i]] = i
        return False

test = Solution()
print(test.containsNearbyDuplicate([1,2,3,1],3))
print(test.containsNearbyDuplicate([1,0,1,1],1))
print(test.containsNearbyDuplicate([1,2,3,1,2,3],2))