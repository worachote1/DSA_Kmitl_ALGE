class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # use: 4 min
        res_arr = []
        nums.sort()
        for i in range(len(nums)):
            if(i != 0 and nums[i] == nums[i-1]):
                continue
            pL = i + 1 
            pR = len(nums) - 1
            while(pL < pR):
                sum_val = nums[pL] + nums[i] + nums[pR]
                if(sum_val > 0):
                    pR -= 1
                elif(sum_val < 0):
                    pL += 1
                else:
                    res_arr.append([nums[pL], nums[i], nums[pR]])
                    pL += 1
                    while(pL < pR and nums[pL] == nums[pL - 1]):
                        pL += 1

        return res_arr