# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    #use binary search
    def searchInsert(self, nums: list[int], target: int) :
        return self.helper(nums,0,len(nums)-1,target)

    def helper(self,nums : list[int],left : int,right : int,target : int):
        if(left<=right):
            mid = (left+right)//2
            if(nums[mid]>target):
                return self.helper(nums,left,mid-1,target)
            elif(nums[mid]<target):
                return self.helper(nums,mid+1,right,target)
            else:
                return mid
        else:
            return left


test = Solution()
print(test.searchInsert([1,3,5,6],5))