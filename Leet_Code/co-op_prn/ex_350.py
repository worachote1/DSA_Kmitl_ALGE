# ex 1
# class Solution(object):
#     def intersect(self, nums1, nums2):
#         res = []
#         data = {}
#         for item in nums1:
#             data[item] = data.get(item,0) + 1
#         for item in nums2:
#             if(item in list(data.keys())):
#                 if(data[item] > 0):
#                     res.append(item)
#                     data[item] = data.get(item,0) - 1
#         return res

# ex 2
class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        nums1.sort()
        nums2.sort()
        p1,p2,len_num1,len_num2 = 0,0,len(nums1),len(nums2)
        while(p1 < len_num1 and p2 < len_num2):
            if(nums1[p1] < nums2[p2]):
                p1 += 1
            elif(nums1[p1] > nums2[p2]):
                p2 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
        return res

test = Solution()
print(test.intersect([1,2,2,1],[2,2]))
print(test.intersect([4,9,5],[9,4,9,8,4]))
        