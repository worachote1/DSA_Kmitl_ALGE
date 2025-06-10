class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # use: 4 min
        temp_dict = {}
        for item in nums:
            if(item not in temp_dict):
                temp_dict[item] = 0
            else:
                temp_dict[item] += 1
        
        cnt = 0
        res = []
        for key, val in sorted(temp_dict.items(), key=lambda item: item[1], reverse=True):
            res.append(key)
            cnt += 1
            if(cnt == k):
                return res
        return res
            
print(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2))