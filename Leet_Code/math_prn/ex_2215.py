class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) :
        ans_0 = []
        ans_1 = []
        nums1.sort()
        nums2.sort()
        for item in nums1:
            if(item in ans_0):
                continue
            if(not self.binary_search(item,0,len(nums2)-1,nums2)):
                ans_0.append(item)
        for item in nums2:
            if(item in ans_1):
                continue
            if(not self.binary_search(item,0,len(nums1)-1,nums1)):
                ans_1.append(item)
        return [ans_0,ans_1]
    def binary_search(self,val : int,left,right,data : list):
        if(left<=right):
            mid = (left + right)//2
            if(data[mid]<val):
                return self.binary_search(val,mid+1,right,data)
            elif(data[mid]>val):
                return self.binary_search(val,left,mid-1,data)
            else:
                return True
        return False

test = Solution()
print(test.findDifference([1,2,3],[2,4,6]))