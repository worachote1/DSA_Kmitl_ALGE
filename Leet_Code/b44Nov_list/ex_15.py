class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]] :
        return self.helper(nums)
    
    def helper(self,nums: list[int]):
        res = []
        nums.sort()
        for i in range(len(nums)):
            pL = i+1
            pR = len(nums)-1            
            while(True):
                if(pL>=pR):
                    break
                sum = nums[pL]+nums[i]+nums[pR]
                if(sum<0):
                    pL+=1
                elif(sum>0):
                    pR-=1
                else:
                    data = [nums[i],nums[pL],nums[pR]]
                    if(data not in res):
                        res.append(data)
                    pL += 1
                    pR -= 1
        return res
