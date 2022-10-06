
def insertionSort(arr):
    for i in range(1,len(arr)):
        curVal = arr[i];
        j = i-1
        while(j>=0 and curVal<arr[j]):
            arr[j+1] = arr[j] 
            j-=1
        
        arr[j+1]=curVal

    return arr

array = [8,5,2,9,5,6,3]
print(insertionSort(array))