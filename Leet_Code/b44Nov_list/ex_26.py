class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if(len(nums)==0):
            return 0
        i=0 
        j = 0
        while(j<len(nums)):
            if(nums[j] not in nums[:j]):
                nums[i] = nums[j]
                i+=1
                j+=1
            else:
                j+=1
        
        return i