from pickletools import read_int4
import numpy as np
#Give an image represented by an NxN matrix
#wirte a method to rotate the image by 90 degrees

metrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
metrix2 = np.array([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
def rotate(metrix):
    n = len(metrix);
    for layer in range(n//2):
        first = layer;
        last = n-1-layer;
        for i in range(first,last):
            top = metrix[layer][i];
            # move left to top
            metrix[layer][i] = metrix[-1-i][layer];
            # move bottom to left
            metrix[-1-i][layer] = metrix[-1-layer][-1-i];
            # move right to bottom
            metrix[-1-layer][-1-i]=metrix[i][-1-layer]
            #finally move top to right
            metrix[i][-1-layer]=top;
    return metrix

print("Before rotate")
print(metrix1)
print(metrix2)

print("After rotate")
print(rotate(metrix1))
print(rotate(metrix2))
