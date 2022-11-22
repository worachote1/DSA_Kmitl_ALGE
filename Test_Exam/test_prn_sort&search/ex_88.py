class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) :
        temp_nums1 = [nums1[i] for i in range(m)]
        k,Pm,Pn=0,0,0
        while(Pm < m and Pn < n):
            if(temp_nums1[Pm]<=nums2[Pn]):
                nums1[k]=temp_nums1[Pm]
                k+=1
                Pm+=1
            elif(nums2[Pn]<=temp_nums1[Pm]):
                nums1[k]=nums2[Pn]
                k+=1
                Pn+=1
        while(Pm < m):
                nums1[k]=temp_nums1[Pm]
                k+=1
                Pm+=1
        while(Pn < n):
                nums1[k]=nums2[Pn]
                k+=1
                Pn+=1              

