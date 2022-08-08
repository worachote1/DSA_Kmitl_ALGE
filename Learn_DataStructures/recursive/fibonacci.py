def f(n):
    if(int(n)!=n or n<0):
        return "ERROR";
    if(n in [0,1]):
        return n;
    return f(n-1)+f(n-2);

print(f(1.5));