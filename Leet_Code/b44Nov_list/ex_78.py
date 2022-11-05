class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        return self.helper(nums,len(nums)-1)
    
    def helper(self,nums,idx):
        if(idx<0):
            return [[]]
        
        subset = self.helper(nums,idx-1)
        n = len(subset)
        for i in range(n):
            subset.append(subset[i]+[nums[idx]])
        
        return subset

