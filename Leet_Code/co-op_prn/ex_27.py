class Solution(object):
    def removeElement(self, nums, val):
        j = 0
        for i in range(0,len(nums)):
            if(nums[i] != val):
                nums[j] = nums[i]
                j += 1
        return j
    
test = Solution()
print(test.removeElement([3,2,2,3],3)) # Output: 2, nums = [2,2,_,_]
print(test.removeElement([0,1,2,2,3,0,4,2],2)) #5, nums = [0,1,4,0,3,_,_,_]