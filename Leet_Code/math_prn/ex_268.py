class Solution:
    def missingNumber(self, nums: list[int]) :
        nums.sort()
        x = 0
        k = 0
        while(k<=len(nums)-1):
            if(x!=nums[k]):
                break
            k+=1
            x+=1
        return x
        
test = Solution()
print(test.missingNumber([3,0,1]))
print(test.missingNumber([0,1]))
print(test.missingNumber([9,6,4,2,3,5,7,0,1]))