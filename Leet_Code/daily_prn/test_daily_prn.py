def getPermutations(array):
    # Write your code here.
    perm_all = []
    if(len(array)==0):
        return perm_all
    helper(array,[],perm_all)
    return perm_all

def helper(arr,perm_cur,perm_all):
    if(len(arr)==0):
        perm_all.append(perm_cur)
    for i in range(len(arr)):
        newArr = arr[:i]+arr[i+1:]
        k = perm_cur + [arr[i]]
        helper(newArr,k,perm_all)

print(getPermutations([1,2,3]))
print(getPermutations([1,0]))