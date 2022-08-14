#find maximum product of two int in array where all elements are positive
import sys
from tkinter.tix import INTEGER
import numpy as np

myArray = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])

def findMaxproduct(array):
    max = array[0]*array[1];
    pair = "";
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if(max<array[i]*array[j]):
                max = array[i]*array[j];
                pair = "pair ->("+str(array[i])+","+str(array[j])+")";
    return str(max)+" "+pair;

print(findMaxproduct(myArray));


