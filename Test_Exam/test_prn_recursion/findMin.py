# ***in Real exam
def findmin_recur(arr):
    return helper(arr,len(arr)-1)

def helper(arr,index):
    if(index<0):
        return arr[index+1]
    
    min = helper(arr,index-1)
    return min if min<arr[index] else arr[index]

arr = [8,5,2,9,6]
arr2 = [7,2,-4,8,4,-2,6,9,8,-4,1,2,0,5]
print(findmin_recur(arr))
print(findmin_recur(arr2))