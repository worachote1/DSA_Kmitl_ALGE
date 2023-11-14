class Solution(object):
    def subarraySum(self, nums, k):
        data = {0 : 1}
        cur_sum = 0
        res_cnt = 0
        for item in nums:
            cur_sum += item
            if (data.get(cur_sum-k)):
                res_cnt += data.get(cur_sum-k)
            data[cur_sum] = data.get(cur_sum,0) + 1
        return res_cnt

test = Solution()
print(test.subarraySum([1,1,1],2))
print(test.subarraySum([1,2,3],3))
# err case
print(test.subarraySum([1],0))
print(test.subarraySum([1,-1,0],0))