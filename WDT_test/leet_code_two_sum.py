class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # use: 4 min
        diff_dict = {}
        for idx, item in enumerate(nums):
            if(item in diff_dict):
                return [diff_dict[item], idx]
            diff_val = target - item
            if(diff_val not in diff_dict):
                diff_dict[diff_val] = idx