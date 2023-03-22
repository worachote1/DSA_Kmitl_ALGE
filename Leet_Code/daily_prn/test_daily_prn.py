class Solution:
    def zeroFilledSubarray(self, nums):
        cnt_zero,res = 0,0
        for item in nums:
            if(item==0):
                cnt_zero += 1
                continue
            res += (cnt_zero*(cnt_zero+1))//2
            cnt_zero = 0
        res += (cnt_zero*(cnt_zero+1))//2
        return res

test = Solution()
print(test.zeroFilledSubarray([0])) 
print(test.zeroFilledSubarray([0,0]))
print(test.zeroFilledSubarray([0,0,0]))

print(test.zeroFilledSubarray([1,3,0,0,2,0,0,4]))   
print(test.zeroFilledSubarray([0,0,0,2,0,0]))   
print(test.zeroFilledSubarray([2,10,2019]))   