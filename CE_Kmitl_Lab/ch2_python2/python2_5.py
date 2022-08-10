def bon(w):
    ## Enter Your Code Here ###
    decode = 0;
    stop = False;
    for i in range (len(w)-1):
        for j in range (i+1,len(w)):
            if(w[j].lower()==w[i].lower()):
                decode = ord(w[i].lower())-ord('a')+1;
                stop = True;
        if(stop):
            break;
    return decode*4;    
secretCode = input("Enter secret code : ")
print(bon(secretCode))

# print(ord('c')-ord('a'));
# print('s'.upper());