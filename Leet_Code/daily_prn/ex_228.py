class Solution(object):
    def summaryRanges(self, nums):
        Idx,n,res = 0,len(nums),[]
        while(Idx<n):
            temp,j = [nums[Idx]],Idx+1
            while(j<n):
                x = temp[-1]
                if(x==nums[j] or x==nums[j]-1):
                    temp.append(nums[j])
                    j+=1
                else:
                    break
            Idx = j
            temp2 = list(set(temp))
            temp2.sort()
            # print("temp2 prn : ",temp2)
            if(len(temp2)>1):
                res.append(str(temp2[0])+"->"+str(temp2[-1]))
            else:
                res.append(str(temp2[0]))
        return res
    
test = Solution()
print(test.summaryRanges([0,1,2,4,5,7]))
print(test.summaryRanges([0,2,3,4,6,8,9]))
print(test.summaryRanges([7,8]))
