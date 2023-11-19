class Solution(object):
    def searchInsert(self, nums, target):
        def hepler(pL,pR):
            mid = (pL + pR)//2
            if(pL <= pR):
                if(nums[mid] < target):
                    return hepler(mid + 1,pR)
                elif(nums[mid] > target):
                    return hepler(pL,mid - 1)
                else:
                    return mid
            return pL
        return hepler(0,len(nums)-1)

test = Solution()
print(test.searchInsert([1,3,5,6],5))
print(test.searchInsert([1,3,5,6],2))
print(test.searchInsert([1,3,5,6],7))