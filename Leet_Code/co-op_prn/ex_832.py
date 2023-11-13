class Solution(object):
    def flipAndInvertImage(self, image):
        self.flip(image)
        self.invert(image)
        return image; 
    
    def flip(self, arr):
        len_arr = len(arr)
        for i in range(0,len_arr):
            for j in range(0,len_arr//2):
                temp = arr[i][len_arr-1-j]
                arr[i][len_arr-1-j] = arr[i][j]
                arr[i][j] = temp   
    def invert(self, arr):
        len_arr = len(arr)
        len_arr_col = len(arr[0])
        for i in range(0,len_arr):
            for j in range(0,len_arr_col):
                if(arr[i][j] == 1):
                    arr[i][j] = 0
                else:
                    arr[i][j] = 1
        
test = Solution();
print(test.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(test.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))