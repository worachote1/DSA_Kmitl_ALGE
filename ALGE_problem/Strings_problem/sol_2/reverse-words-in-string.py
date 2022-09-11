def reverseWordsInString(string):
    
    res = [];
    pR = len(string)-1
    for i in range(len(string)-1,-1,-1):
        
        if(i==0):
            res.append(string[i:pR+1])  
            break;
        if(string[i]!=" "):
            pass;
        elif(string[i]==" "):
            res.append(string[i+1:pR+1])
            pR=i-1;
              
    return " ".join(res);

string1 = "AlgoExpert is the best!"
print(reverseWordsInString(string1))