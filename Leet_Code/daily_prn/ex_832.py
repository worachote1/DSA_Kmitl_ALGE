# 832. Flipping an Image
class Solution(object):
    def flipAndInvertImage(self, image):
        for item in image:
            self.render(item)
        return image

    def render(self,arr):
        self.reverse(0,len(arr)-1,arr)
        self.invert(arr)
    
    def reverse(self,left_Idx,right_Idx,arr):
        while(left_Idx<right_Idx):
            arr[left_Idx],arr[right_Idx] = arr[right_Idx],arr[left_Idx]
            left_Idx,right_Idx=left_Idx+1,right_Idx-1
        
    def invert(self,arr):
        for i in range(len(arr)):
            arr[i] = (arr[i]+1) % 2
    
test = Solution()
print(test.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(test.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))