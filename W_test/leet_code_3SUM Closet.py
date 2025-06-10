class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # use: 8 min
        res_val = float('inf')
        nums.sort()
        for i in range(len(nums)):
            # if(i != 0 and nums[i] > nums[i-1]):
            #     continue
            pL = i + 1
            pR = len(nums) - 1
            while(pL < pR):
                sum_val = nums[pL] + nums[i] + nums[pR]
                cur_diff = abs(target-sum_val)
                cur_res_diff = abs(target-res_val)

                if(cur_diff < cur_res_diff):
                    res_val = sum_val

                if(sum_val < target):
                    pL += 1
                elif(sum_val > target):
                    pR -= 1
                else:
                    return target
                
        return res_val