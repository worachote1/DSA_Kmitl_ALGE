class Solution:
    def frequencySort(self, s: str) :
        data_occur = {}
        list_occur = [[] for i in range(len(s)+1)]
        for item in s:
            data_occur[item] = 1 + data_occur.get(item,0)
        
        for key,val in data_occur.items():
            list_occur[val].append(key)

        res=""
        for i in range(len(list_occur)-1,0,-1):
            if(list_occur[i]==[]):
                continue
            for item in list_occur[i]:
                res += item * i
        
        return res

test = Solution()
print(test.frequencySort("tree"))