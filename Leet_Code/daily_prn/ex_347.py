class Solution:
    def topKFrequent(self, nums: list[int], k: int) :
        data_occur = {}
        list_occur = [[] for item in range(len(nums)+1)]
        for item in nums:
            if(item not in data_occur):
                data_occur[item]=1
            else:
                data_occur[item]+=1
        #print(data_occur)
        for item in data_occur:
            list_occur[data_occur[item]].append(item)
        counter = 0
        res = []
        # print("prn list : ")
        #print(list_occur)
        for i in range(len(list_occur)-1,-1,-1):
            if(list_occur[i]==[]):
                continue
            for item in list_occur[i]:
                res.append(item)
                counter+=1
                if(counter == k):
                    return res
                     
test = Solution()
print(test.topKFrequent([1,1,1,2,2,3],2))
print(test.topKFrequent([4,1,-1,2,-1,2,3],2))