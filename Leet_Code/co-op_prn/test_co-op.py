# class Solution(object):
#     def combinationSum(self, candidates, target):
#         res = []
#         curArr = []
#         def  dfs(Idx,curTarget):
#             if(curTarget == target):
#                 res.append([item for item in curArr])
#                 return
#             if(curTarget > target):
#                 return
#             if(Idx >= len(candidates)):
#                 return
#             curArr.append(candidates[Idx])
#             dfs(Idx,curTarget+candidates[Idx])
#             curArr.pop()
#             dfs(Idx+1,curTarget)
#         dfs(0,0)
#         return res
# test = Solution()
# print(test.combinationSum([2,3,6,7],7))
# print(test.combinationSum([2,3,5],8))
# print(test.combinationSum([2],1))

# class Solution(object):
#     def combinationSum2(self, candidates, target):
#         res = []
#         curArr = []
#         data = {}
#         candidates.sort()
#         for item in candidates:
#             data[item] = data.get(item,0) + 1
        
#         def dfs(Idx,curTarget):
#             if(curTarget == target):
#                 res.append([item for item in curArr])
#                 return
#             if(curTarget > target):
#                 return
#             if(Idx >= len(data)):
#                 return
#             curDataKey = list(data.keys())[Idx] 
#             if(data[curDataKey] > 0):
#                 curArr.append(curDataKey)
#                 data[curDataKey] = data.get(curDataKey,0) - 1
#                 dfs(Idx,curTarget + curDataKey)
#                 curArr.pop()
#                 data[curDataKey] = data.get(curDataKey,0) + 1
#             dfs(Idx+1,curTarget)
#         dfs(0,0)
#         return res
    
# test = Solution()
# print(test.combinationSum2([10,1,2,7,6,1,5],8))
# print(test.combinationSum2([2,5,2,1,2],5))

