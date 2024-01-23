class Solution(object):
    def fourSum(self, nums, target):
        res = []
        quad = []
        nums.sort()

        def dfs(k,startIdx,curSum):
            if(k > 2):
                for i in range(startIdx,len(nums)-k+1):
                    if(i > startIdx and nums[i] == nums[i-1]):
                        continue
                    quad.append(nums[i])
                    dfs(k-1,i+1,curSum+nums[i])
                    quad.pop()
            else:
                pL = startIdx
                pR = len(nums) - 1
                while(pL < pR):
                    sumVal = curSum + nums[pL] + nums[pR]
                    if(sumVal < target):
                        pL += 1
                    elif(sumVal > target):
                        pR -= 1
                    else:
                        temp = [item for item in quad]
                        temp += [nums[pL],nums[pR]]
                        res.extend([temp])
                        pL += 1
                        while(pL < pR and nums[pL] == nums[pL-1]):
                            pL += 1
        dfs(4,0,0)
        return res
                
test = Solution()
print(test.fourSum([1,0,-1,0,-2,2],0))
print(test.fourSum([2,2,2,2,2],8))
