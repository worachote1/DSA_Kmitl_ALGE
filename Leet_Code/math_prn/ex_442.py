class Solution:
    def findDuplicates(self, nums: list[int]) :
        l,r,Idx,n = 0,1,0,len(nums)
        nums.sort()
        while(r<n):
            if(nums[l]==nums[r]):
                nums[Idx] = nums[r]
                l = r+1
                r = l+1
                Idx += 1
            else:
                l+=1
                r+=1
        return nums[:Idx]

test = Solution()
print(test.findDuplicates([4,3,2,7,8,2,3,1]))
print(test.findDuplicates([1,1,2]))
print(test.findDuplicates([1]))
print(test.findDuplicates([1,1]))