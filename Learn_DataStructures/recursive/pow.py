def pow(n,i):
    if(i < 0 or int(i)!=i):
        return "ERROR";
    if(i==0 or n==1):
        return 1;
    if(i==1):
        return n;
    
    return n*pow(n,i-1);

print(pow(2,-3));