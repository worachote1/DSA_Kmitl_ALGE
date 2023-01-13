class Solution:
    def permuteUnique(self, nums: list[int]):
        res_perm = []
        data = {}
        for item in nums:
            data[item] = data.get(item,0) + 1
        self.helper(nums,[],res_perm,data)
        return res_perm
    def helper(self,nums : list,perm_cur : list,perm_all : list,data : dict):
        if(len(perm_cur)==len(nums)):
            perm_all.append(perm_cur.copy())
        else:
            for item in data:
                if(data[item] != 0):
                    perm_cur.append(item)
                    data[item]-=1
                    self.helper(nums,perm_cur,perm_all,data)
                    perm_cur.pop()
                    data[item]+=1
        
test = Solution()
print(test.permuteUnique([1,2,3]))
print(test.permuteUnique([1,1,2]))