
count = 0;
temp_hight = [9, 11, 7, 9, 7, 1];
#loop from last to index 1
if(len(temp_hight)==1):
    count+=1;
else:
    for i in range(len(temp_hight)-1, 0-1, -1):
        temp_hight_2 = [];
        if(i==len(temp_hight)-1):
            count+=1;
            print("first prn "+str(i)+" which is : "+str(temp_hight[i]));
            continue;
        passCheck = temp_hight[i+1:];
        print(passCheck);
        check = True;
        for j in passCheck:
            if(temp_hight[i]<=j):
                check = False;
                break;
        #count+=1;
        if(check):
            count+=1;
            print("prn "+str(i)+" which is : "+str(temp_hight[i]));
        
    #check at index 0
    # if(temp_hight[0]>temp_hight[1]):
    #     count+=1;
    #     print("last prn "+str(i)+" which is : "+str(temp_hight[0]));
print(count);