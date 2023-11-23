class Solution(object):
    def permuteUnique(self, nums):
        res = []
        perm = []
        data = {}
        for item in nums:
            data[item] = data.get(item,0) + 1
        def dfs():
            if(len(perm)==len(nums)):
                res.append([item for item in perm])
                return
            for item in list(data.keys()):
                if(data[item] > 0):
                    perm.append(item)
                    data[item] = data.get(item,0) - 1
                    dfs()  
                    perm.pop()
                    data[item] = data.get(item,0) + 1
        dfs()
        return res



test = Solution()
print(test.permuteUnique([1,1,2]))
print(test.permuteUnique([1,2,3]))