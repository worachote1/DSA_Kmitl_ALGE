class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) :
        
        res = []
        nums2.sort()
        for item in nums1 :
            if(item in res):
                continue
            if(self.binary_search(item,0,len(nums2)-1,nums2)):
                res.append(item)
            
        return res
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
print(test.intersection([4,9,5],[9,4,9,8,4]))
print(test.intersection([1,2,2,1],[2,2]))