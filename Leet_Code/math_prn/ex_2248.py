class Solution:
    def intersection(self, nums) :
        data = {}
        res = []
        n = len(nums)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                data[nums[i][j]] = data.get(nums[i][j],0) + 1
                if(data[nums[i][j]]==n):
                    res.append(nums[i][j])
        return sorted(res)

test = Solution()
print(test.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
print(test.intersection([[1,2,3],[4,5,6]]))