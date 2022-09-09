def convertDectoBi(arr,Idx,last):
    if(Idx>last):
        print("".join(arr));
        return;
    
    arr[Idx]="0";
    convertDectoBi(arr,Idx+1,last);
    
    arr[Idx]="1";
    convertDectoBi(arr,Idx+1,last);

    
inp = int(input("Enter Number : "));
if(inp<0):
    print('Only Positive & Zero Number ! ! !');
    exit();

#start at 0...inp
if(inp==0):
    arr = ['0'];
else:
    arr = ['0']*inp;
convertDectoBi(arr,0,inp-1);