class Solution:
    def topKFrequent(self, words: list[str], k: int) :
        data_occur = {}
        list_occur = [[] for item in range(len(words)+1)]
        words.sort()
        for item in words:
            data_occur[item] = data_occur.get(item,0) +1 
        
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
print(test.topKFrequent(["i","love","leetcode","i","love","coding"],2))
print(test.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"],4))
