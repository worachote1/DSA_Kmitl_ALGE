def sort(arr):
    insertion_recur(arr,len(arr));
def insertion_recur(arr,n):
    if(n<=1):
        return;
    insertion_recur(arr,n-1);
    #insert then push currentVal in the correct index
    currentVal = arr[n-1];
    j = n-2;
    while(j>=0 and arr[j]<currentVal):
        arr[j+1]=arr[j];
        j-=1;
    arr[j+1]=currentVal;

    
array = [8,5,2,9,5,6,3]
sort(array)
print(array)