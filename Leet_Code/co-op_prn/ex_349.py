class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        set_num1 = set(nums1)
        for item in nums2:
            if(item in list(set_num1)):
                res.append(item)
                set_num1.remove(item)
        return res
    
test = Solution()
print(test.intersection([1,2,2,1],[2,2]))
print(test.intersection([4,9,5],[9,4,9,8,4]))