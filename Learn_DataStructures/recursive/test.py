def  fac(n):
    assert n>=0 and int(n) == n , "Can't find fac !";
    if(n==0):
        return 1;

    return n*fac(n-1);

print(fac(1.5));