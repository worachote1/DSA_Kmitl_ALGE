class Solution(object):
    def construct2DArray(self, original, m, n):
        if(m*n != len(original)):
            return []
        new_arr,Idx,cnt_col = [[] for item in range(m)],0,0
        for i in range(len(original)):
            new_arr[Idx].append(original[i])
            cnt_col+=1
            if(cnt_col==n):
                Idx,cnt_col=Idx+1,0
        return new_arr

test = Solution()
print(test.construct2DArray([1,2,3,4],2,2))
print(test.construct2DArray([1,2,3],1,3))