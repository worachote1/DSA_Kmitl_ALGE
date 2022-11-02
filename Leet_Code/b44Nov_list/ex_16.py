class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        return self.helper(nums,target)

    def helper(self, nums: list[int], target: int):
        closet_data = float('inf')
        nums.sort()
        
        for i in range(len(nums)):
            pL = i+1
            pR = len(nums)-1

            while(True):
                if(pL>=pR):
                    break

                sum = nums[i]+nums[pL]+nums[pR]
                if(abs(sum-target)<abs(closet_data-target)):
                    closet_data = sum            
                #check negative of target to shift pointer
                if(sum==target):
                    return sum                
                elif(sum < target):
                    pL += 1
                elif(sum > target):
                    pR-=1
        return closet_data