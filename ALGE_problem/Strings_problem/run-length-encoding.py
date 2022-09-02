def runLengthEncoding(string):
    count = 0;
    res = [];
    for i in range(len(string)):

        count+=1;
        if(i==len(string)-1):
            res.append(str(count));
            res.append(string[i]);
            continue;
        if(count>=9):
            res.append(str(9));
            res.append(string[i]);
            count=0;
            continue;

        if(string[i]!=string[i+1]):
            res.append(str(count));
            res.append(string[i]);
            count=0;
    
    return "".join(res);

print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"));