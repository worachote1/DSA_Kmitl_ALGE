class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]] :
        pass
    def helper(self,nums: list[int]):
        res = []
        nums.sort()
        for i in range(len(nums)):
            pL = 0
            pR = len(nums)-1


