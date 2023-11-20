# sol 1 : using loop (o(n^3))
# class Solution(object):
#     def fourSum(self, nums, target):
#         res = []
#         nums.sort()
#         for i in range(0,len(nums)-3):
#             if(i != 0 and nums[i] == nums[i-1]):
#                 continue
#             for j in range(i+1,len(nums)-2):
#                 if(j != i+1 and nums[j] == nums[j-1]):
#                     continue
#                 pL,pR = j + 1,len(nums)-1
#                 while(pL < pR):
#                     sumVal = nums[i]+nums[j]+nums[pL]+nums[pR]
#                     if(sumVal < target):
#                         pL += 1
#                     elif(sumVal > target):
#                         pR -= 1
#                     else:
#                         quadruplet = [nums[i],nums[j],nums[pL],nums[pR]]
#                         res.append(quadruplet)
#                         pL += 1
#                         while(pL < pR and nums[pL] == nums[pL-1]):
#                             pL += 1
#         return res
    
# sol2 : using recursion(o(n^3)) can be use with any k sum 
class Solution(object):
    def fourSum(self, nums, target):
        res = []
        quadruplet = []
        nums.sort()
        def kSum(k,startIdx,target):
            if(k != 2):
                for i in range(startIdx,len(nums)-k+1):
                    if(i != startIdx and nums[i] == nums[i-1]):
                        continue
                    quadruplet.append(nums[i])
                    kSum(k-1,i+1,target-nums[i])
                    quadruplet.pop()
                    
            else:
                pL,pR = startIdx,len(nums)-1
                while(pL < pR):
                    sumVal = nums[pL] + nums[pR]
                    if(sumVal < target):
                        pL += 1
                    elif(sumVal > target):
                        pR -= 1
                    else:
                        temp_quad = [item for item in quadruplet]
                        temp_quad += [nums[pL],nums[pR]]
                        res.append(temp_quad)
                        pL += 1
                        while(pL < pR and nums[pL] == nums[pL-1]):
                            pL += 1

        kSum(4,0,target)
        return res
    
test = Solution()
print(test.fourSum([1,0,-1,0,-2,2],0))
print(test.fourSum([2,2,2,2,2],8))
#err case
print(test.fourSum([-2,-1,-1,1,1,2,2],0))