class Solution(object):
    def summaryRanges(self, nums):
        Idx,n,res = 0,len(nums),[]
        while(Idx<n):
            startVal= nums[Idx]
            while(Idx<n-1):
                if(nums[Idx]==nums[Idx+1]-1):
                    Idx+=1
                else:
                    break
            endVal = nums[Idx]
            if(startVal==endVal):
                res.append(str(endVal))
            else:
                res.append(str(startVal)+"->"+str(endVal))
            Idx += 1
        return res
    
test = Solution()
print(test.summaryRanges([0,1,2,4,5,7]))
print(test.summaryRanges([0,2,3,4,6,8,9]))
print(test.summaryRanges([7,8]))
