class Solution(object):
    def searchRange(self, nums, target):
        pL,pR = 0,len(nums)-1
        while(pL <= pR):
            if(nums[pL] == target and nums[pR] == target):
                return [pL,pR] 
            if(nums[pL] != target):
                pL += 1
            if(nums[pR] != target):
                pR -= 1
        return [-1,-1]

test = Solution()
# print(test.searchRange([5,7,7,8,8,10],8))
# print(test.searchRange([5,7,7,8,8,10],6))
# print(test.searchRange([],0))
# err case
print(test.searchRange([1],1)) # [0,0]