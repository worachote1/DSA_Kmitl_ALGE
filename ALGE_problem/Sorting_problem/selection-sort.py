def selectionSort(array):
    
    
 for i in range (len(array)):
       maxIdx = 0
       for j in range (len(array)-i):
           if array[maxIdx]<array[j] :
               maxIdx = j

       temp = array[len(array)-1-i]
       array[len(array)-1-i] = array[maxIdx]
       array[maxIdx]=temp
 return array
