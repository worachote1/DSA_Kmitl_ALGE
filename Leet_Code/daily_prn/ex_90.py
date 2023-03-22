class Solution(object):
    def subsetsWithDup(self, nums):
        res,temp,n=[],[],len(nums)
        nums.sort()
        def helper(Idx):
            if(Idx>n-1):
                res.append([item for item in temp])
                return
            temp.append(nums[Idx])
            helper(Idx+1)
            temp.pop()
            while(Idx+1 < n and nums[Idx] == nums[Idx+1]):
                Idx+=1
            helper(Idx+1)
        
        helper(0)
        return res
    
test = Solution()
print(test.subsetsWithDup([1,2,2]))
print(test.subsetsWithDup([0]))
# err 
print(test.subsetsWithDup([4,4,4,1,4]))
                