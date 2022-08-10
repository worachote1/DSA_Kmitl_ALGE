def capitalizeFirst(arr):
    res = [];
    if(len(arr)==0):
        return res;
    res.append(arr[0][0].upper()+arr[0][1:]);
    return res + capitalizeFirst(arr[1:]);
    
   
print(capitalizeFirst(['car', 'taco', 'banana'])); # ['Car','Taco','Banana']    

test = [2,5,87,94];

print(test[4:]);