class Solution(object):
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        for i in range(0,len(nums)-3):
            if(i != 0 and nums[i] == nums[i-1]):
                continue
            for j in range(i+1,len(nums)-2):
                if(j != i+1 and nums[j] == nums[j-1]):
                    continue
                pL,pR = j + 1,len(nums)-1
                while(pL < pR):
                    sumVal = nums[i]+nums[j]+nums[pL]+nums[pR]
                    if(sumVal < target):
                        pL += 1
                    elif(sumVal > target):
                        pR -= 1
                    else:
                        quadruplet = [nums[i],nums[j],nums[pL],nums[pR]]
                        res.append(quadruplet)
                        pL += 1
                        while(pL < len(nums) and nums[pL] == nums[pL-1]):
                            pL += 1
        return res
    
test = Solution()
print(test.fourSum([1,0,-1,0,-2,2],0))
print(test.fourSum([2,2,2,2,2],8))
#err case
print(test.fourSum([-2,-1,-1,1,1,2,2],0))