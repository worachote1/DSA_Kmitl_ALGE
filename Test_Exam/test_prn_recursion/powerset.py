# def powerset(array):
#     subsets = [[]]
#     for i in array:
#         for j in range(len(subsets)):
#             cur = subsets[j]
#             subsets.append(cur+[i])

#     return subsets
    
arr = [1,2,3]

# for loop
def powerset_for(arr):
    subsets = [[]]
    for i in range(len(arr)):
        for j in range(len(subsets)):
            cur = subsets[j]
            subsets.append(cur+[arr[i]])
            
            
    return subsets

#recursive
def powerset_recur(arr):
    return helper(arr,len(arr)-1)

def helper(arr,index):
    if(index<0):
        return [[]]
    
    subsets = helper(arr,index-1)
    for i in range(len(subsets)):
        subsets.append(subsets[i]+[arr[index]])
    return subsets

#print(powerset_for(arr))
print(powerset_recur(arr))
