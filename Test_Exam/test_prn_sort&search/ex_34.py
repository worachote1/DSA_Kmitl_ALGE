class Solution:
    def searchRange(self, nums: list[int], target: int) :
        res = [-1,-1]
        res[0] = self.helperfindLeft(nums,target,0,len(nums)-1)
        res[1] = self.helperfindRight(nums,target,0,len(nums)-1)
        return res
    def helperfindLeft(self,nums: list[int],target : int,left : int,right : int):
        k = -1
        while(left<=right):
            mid = (left+right)//2
            if(nums[mid]<target):
                left = mid + 1
            elif(nums[mid]>target):
                right = mid - 1
            else:
                k = mid
                right = mid - 1
        return k

    def helperfindRight(self,nums: list[int],target : int,left : int,right : int):
        k = -1
        while(left<=right):
            mid = (left+right)//2
            if(nums[mid]<target):
                left = mid + 1
            elif(nums[mid]>target):
                right = mid - 1
            else:
                k = mid
                left = mid + 1
        return k

test = Solution()
print(test.searchRange([5,7,7,8,8,10],8))
print(test.searchRange([],0))
print(test.searchRange([5,7,7,8,8,10],6))