# sol. 1
# class Solution(object):
#     def threeSum(self, nums):
#         res = []
#         nums.sort()
#         for i in range(len(nums)):
#             pL,pR = 0, len(nums)-1
#             while(pL < i and pR > i):
#                 sum_val = nums[pL] + nums[i] + nums[pR]
#                 if(sum_val < 0):
#                     pL += 1
#                 elif(sum_val > 0):
#                     pR -= 1
#                 else:
#                     triplet = [nums[pL],nums[i],nums[pR]]
#                     if triplet not in res:
#                         res.append(triplet)
#                     pL,pR = pL+1,pR-1
#         return res
    
#sol. 2
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            pL = i + 1
            pR = len(nums)-1
            while(pL < pR):
                sumVal = nums[i] + nums[pL] + nums[pR]
                if(sumVal < 0):
                    pL += 1
                elif(sumVal > 0):
                    pR -= 1
                else:
                    triplet = [nums[i],nums[pL],nums[pR]]
                    res.append(triplet)
                    pL += 1
                    while(pL < pR and nums[pL] == nums[pL-1]):
                        pL += 1    
        return res
    
test = Solution()
print(test.threeSum([-1,0,1,2,-1,-4]))
print(test.threeSum([0,1,1]))
print(test.threeSum([0,0,0]))