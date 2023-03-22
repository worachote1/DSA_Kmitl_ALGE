class Solution(object):
    def subsets(self, nums):
        res,n = [],len(nums)        
        temp = []
        def hepler(Idx):
            if(Idx>n-1):
                res.append([item for item in temp])
                return
            temp.append(nums[Idx])
            hepler(Idx+1)
            temp.pop()
            hepler(Idx+1)

        hepler(0)
        return res

test = Solution()
print(test.subsets([1,2,3]))
print(test.subsets([0]))


