from array import *;
arrayName = array('i',[1,2,3,44,68,99,122]);
def binarySearch(arr,low,hight,value):
    mid = (low+hight)//2;
    if(value==arr[mid]):
        return mid
    if(value>arr[mid]):
        return binarySearch(arr,mid+1,hight,value)
    elif(value<arr[mid]):
        return binarySearch(arr,0,mid-1,value)
    
print(arrayName)
print(binarySearch(arrayName,0,len(arrayName)-1,44))