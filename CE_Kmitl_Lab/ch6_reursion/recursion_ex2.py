def reverse_sort(arr):
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


inp = input("Enter your List : ").split(",");
arr = [int(item) for item in inp];
# print(inp);
# print(arr);
reverse_sort(arr);
print("List after Sorted : {0}".format(arr));