class Solution:
    # Solution I
    # def singleNumber(self, nums: list[int]):
    #     Idx,n = 0,len(nums)
    #     nums.sort()
    #     while(Idx<n-2):
    #         if(nums[Idx]==nums[Idx+1]==nums[Idx+2]):
    #             Idx += 3
    #         else:
    #             return nums[Idx]
    #     return nums[-1]

    # Solution II : bit manipulation
    def singleNumber(self, nums: list[int]):
        one,two = 0,0
        for item in nums:
            one = (one^item) & (~two)
            two = (two^item) & (~one)
        return one
test = Solution()
print(test.singleNumber([2,2,3,2]))
print(test.singleNumber([0,1,0,1,0,1,99]))
