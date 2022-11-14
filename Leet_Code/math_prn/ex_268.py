class Solution:
    def missingNumber(self, nums: list[int]) :
        n = len(nums)
        series_sum = n*(n+1)//2
        for item in nums:
            series_sum -= item

        return series_sum
        
test = Solution()
print(test.missingNumber([3,0,1]))
print(test.missingNumber([0,1]))
print(test.missingNumber([9,6,4,2,3,5,7,0,1]))