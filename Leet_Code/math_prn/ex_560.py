class Solution:
    def subarraySum(self, nums: list[int], k: int) :
        ans= 0
        preSum = 0
        dic = {}
        dic[0] = 1
        for i in nums:
            preSum += i
            if preSum-k in dic:
                ans+=dic[preSum-k]
            if(preSum not in dic):
                dic[preSum]=1
            else:
                dic[preSum] +=1 
        return ans

test = Solution()
print(test.subarraySum([10,2,-2,-20,10],-10))