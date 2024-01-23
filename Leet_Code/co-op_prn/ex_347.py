class Solution(object):
    def topKFrequent(self, nums, k):
        data = {}
        n = len(nums)
        res = []
        res_temp = [[] for i in range(n+1)]
        for item in nums:
            data[item] = data.get(item,0) + 1
        for item in data:
            res_temp[data[item]].append(item)
        print(data)
        print(res_temp)
        for i in reversed(range(len(res_temp))):
            for item in res_temp[i]:
                res.append(item)
                k -= 1
                if(k==0):
                    return res
                
test = Solution()
# print(test.topKFrequent([1,1,1,2,2,3], 2))
# print(test.topKFrequent([1],1))
# # err case 
# print(test.topKFrequent([1,2],2))
print(test.topKFrequent([1,1,1,2,2,3],2))
