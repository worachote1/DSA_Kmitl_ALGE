def findThreeLargestNumbers(array):
    # Write your code here.
    res_threeLargest = [None,None,None]
    for item in array:
        update(res_threeLargest,item)
    return res_threeLargest

def update(res : list,num : int):
    if(res[2]==None or num > res[2]):
        shiftAndUpdate(res,2,num) #todo
    elif(res[1]==None or num > res[1]):
        shiftAndUpdate(res,1,num) #todo
    elif(res[0]==None or num > res[0]):
        shiftAndUpdate(res,0,num) #todo

def shiftAndUpdate(res,Idx,newNum):
    for i in range(Idx+1):
        if(i==Idx):
            res[i]=newNum
        else:
            res[i]=res[i+1]
        
