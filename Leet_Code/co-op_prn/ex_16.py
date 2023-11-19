class Solution(object):
    def threeSumClosest(self, nums, target):
        res = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            pL = i+1
            pR = len(nums)-1
            if(i > 0):
                if(nums[i] == nums[i-1]):
                    continue
            while(pL < pR):
                sumVal = nums[i] + nums[pL] + nums[pR]
                lasted_diff = abs(target-res)
                cur_diff = abs(target - sumVal)
                if(cur_diff < lasted_diff):
                    res = sumVal
                if(sumVal < target):
                    pL += 1
                elif(sumVal > target):
                    pR -= 1
                else:
                    return target
        return res

test = Solution()
print(test.threeSumClosest([-1,2,1,-4],1))
print(test.threeSumClosest([0,0,0],1))
# err case
# print(test.threeSumClosest([0,1,2],0))