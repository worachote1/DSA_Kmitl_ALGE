class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res_permAll = []
        self.helper(nums,[],res_permAll)
        return res_permAll
    def helper(self,nums,perm_cur,perm_all):
        if(len(nums)==0):
            perm_all.append(perm_cur)
        for i in range(len(nums)):
            self.helper(nums[:i]+nums[i+1:],perm_cur+[nums[i]],perm_all)