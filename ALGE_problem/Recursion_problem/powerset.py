#Solution 1
# def powerset(array):
#     res = [[]];
#     for item in array:
#         for i in range(len(res)):
#             res.append(res[i]+[item]);

#     return res;

#Solution 2 : recursion
def powerset(array,Idx=None):
    
    if(Idx is None):
        Idx = len(array)-1;
    if(Idx < 0):
        return [[]];
    
    #print("Idx-1 -> ",Idx-1);
    subSet = powerset(array,Idx-1);

    for i in range(len(subSet)):
        #print("44 -> ",subSet[i]);
        subSet.append(subSet[i]+[array[Idx]]);
        #print("45 -> ",subSet[i]+[array[Idx]]);

    
    return subSet;

myArr = [1,2,3];
print(powerset(myArr));
myArr_2 = [];
print(powerset(myArr_2));