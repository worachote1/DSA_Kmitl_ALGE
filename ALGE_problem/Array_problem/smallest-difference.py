#import sys;
def smallestDifference(arrayOne, arrayTwo):
    pointer_1st = 0;
    pointer_2nd = 0;

    arrayOne.sort();
    arrayTwo.sort();
    res = -44;
    temp_res = 4444;
    while(True):
        oneVal = arrayOne[pointer_1st];
        twoVal = arrayTwo[pointer_2nd];
        res = abs(oneVal-twoVal);
        if(res==0):
            return [oneVal,twoVal];
        
        if(temp_res>res):
            temp_res = res;
            temp_arr = [oneVal,twoVal];
        if(oneVal<twoVal):
            pointer_1st+=1;
        elif(twoVal<oneVal):
            pointer_2nd+=1;

        if(pointer_1st > len(arrayOne)-1 or pointer_2nd > len(arrayTwo)-1):
            return temp_arr;

print(smallestDifference([10, 0, 20, 25, 2200],[1005, 1006, 1014, 1032, 1031]));
print(smallestDifference([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17]));