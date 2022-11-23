x = [2,1,3,-4,22,7,15]

def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
        minIdx = i
        for j in range(i+1,len(array)):
            if(array[minIdx]>array[j]):
                minIdx = j
        
        array[minIdx],array[i]=array[i],array[minIdx]
    return array

print(x)
selectionSort(x)
print(x)