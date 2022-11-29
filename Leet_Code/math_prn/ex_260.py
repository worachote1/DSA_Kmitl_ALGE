# 260. Single Number III
class Solution:
    def singleNumber(self, nums: list[int]) :
        aXORb = 0
        for item in nums:
            aXORb = aXORb ^ item
        #d = the most right different bit
        d = aXORb & -aXORb
        res1,res2 = 0,0
        for item in nums:
            if(d & item == 0):
                res1 = res1 ^ item
            else:
                res2 = res2 ^ item
        return [res1,res2]

test = Solution()
print(test.singleNumber([1,2,1,3,2,5]))
print(test.singleNumber([-1,0]))
print(test.singleNumber([0,1]))