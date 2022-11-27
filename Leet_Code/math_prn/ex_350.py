class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) :
        # use two pointers
        res,i,j=[],0,0
        nums1.sort()
        nums2.sort()
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]<nums2[j]):
                i+=1
            elif(nums2[j]<nums1[i]):
                j+=1
            else:
                res.append(nums1[i])
                i+=1
                j+=1
        return res

test = Solution()
print(test.intersect([1,2,2,1],[2,2]))
print(test.intersect([4,9,5],[9,4,9,8,4]))