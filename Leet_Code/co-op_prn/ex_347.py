class Solution(object):
    def topKFrequent(self, nums, k):
        res = []
        data = {}
        occur_list = [[] for i in range(0,len(nums) + 1)]
        for item in nums:
            data[item] = data.get(item,0) + 1
        for key,val in data.items():
            occur_list[val].append(key)
        for i in reversed(range(0,len(occur_list))):
            for item in occur_list[i]:
                res.append(item)
                if(len(res) == k):
                    return res
                
test = Solution()
print(test.topKFrequent([1,1,1,2,2,3], 2))
print(test.topKFrequent([1],1))
# err case
print(test.topKFrequent([1,2],2))
print(test.topKFrequent([4,1,-1,2,-1,2,3],2))