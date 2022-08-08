def DecToBi(n):
    if(int(n) != n):
        return "ERROR";
    if(n==0):
        return n%2; 
    return (n%2)+10*DecToBi(int(n/2));

print(DecToBi(13));
print(DecToBi(10));
print(DecToBi(1.5));