def productOfArray(arr):
    dot = 1;
    for i in range(0,len(arr)):
        dot *= arr[i];
    return dot

print(productOfArray([1,2,3]));