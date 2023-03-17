class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n if(k>n) else k
        self.helper(0,n-1,nums)
        self.helper(0,k-1,nums)
        self.helper(k,n-1,nums)
        
    def helper(self,left,right,arr):
        while(left<right):
            temp = arr[right]
            arr[right]=arr[left]
            arr[left]=temp
            left,right=left+1,right-1
    
