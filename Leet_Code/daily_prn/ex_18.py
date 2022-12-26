class Solution:
    def fourSum(self, nums: list[int], target: int) :
        data = {}
        res = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sumNum = nums[i]+nums[j]
                diff = target - sumNum
                if(diff in data):
                    for item in data[diff]:
                        k = item+[nums[i],nums[j]]
                        if(k not in res):
                            res.append(k)
            for j in range(0,i):
                sumNum = nums[j]+nums[i]
                m = [nums[j],nums[i]]
                if(sumNum not in data):
                    data[sumNum] = [m]
                else:
                    if(m not in data[sumNum]):
                        data[sumNum].append(m)
        return res

test = Solution()
print(test.fourSum([1,0,-1,0,-2,2],0))
print(test.fourSum([2,2,2,2],8))