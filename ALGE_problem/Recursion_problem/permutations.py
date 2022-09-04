
def getPermutations(array):
    permutations_All = [];
    permutations_Helper(array,[],permutations_All);
    return permutations_All;

def permutations_Helper(array,current_perm,perm_All):
    if(len(array)==0 and len(current_perm)!=0):
        #print("44 -> ",current_perm);
        perm_All.append(current_perm);
    else:
        for i in range(len(array)):
            newArr = array[:i]+array[i+1:];
            newPerm = current_perm+[array[i]];
            permutations_Helper(newArr,newPerm,perm_All);


myArr = [1,2,3];
print("prn ----------");
print(getPermutations(myArr));