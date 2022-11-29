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

    # Solution II : bit manipulation (best run time)
    # def singleNumber(self, nums: list[int]):
    #     one,two = 0,0
    #     for item in nums:
    #         one = (one^item) & (~two)
    #         two = (two^item) & (~one)
    #     return one

    # Solution III : bit shift prn
    def singleNumber(self, nums: list[int]):
        res = 0
        for i in range(32):
            count = 0
            k = 1<<i
            for item in nums:
                count += (item & k)
            count %= 3
            if(i==31 and count!=0):
                #now k is also = 2**31
                res = res - 2**31
                continue
            res = res | k if count!=0 else res
        return res

test = Solution()
print(test.singleNumber([2,2,3,2]))
print(test.singleNumber([0,1,0,1,0,1,99]))

# error test case
# In some languages such as python it will give wrong answer in case of negative elements.
print(test.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))
