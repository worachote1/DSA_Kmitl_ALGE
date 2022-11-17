class Solution:
    def topKFrequent(self, nums: list[int], k: int) :
        data_occur = {}
        list_occur = [[] for item in range(len(nums)+1)]
        for item in nums:
            data_occur[item] = 1+data_occur.get(item,0)
        for key,val in data_occur.items():
            list_occur[val].append(key)
        res = []
        for i in range(len(list_occur)-1,0,-1):
            if(list_occur[i]==[]):
                continue
            for item in list_occur[i]:
                res.append(item)
                if(len(res)==k):
                    return res

test = Solution()
print(test.topKFrequent([1,1,1,2,2,3],2))
print(test.topKFrequent([4,1,-1,2,-1,2,3],2))