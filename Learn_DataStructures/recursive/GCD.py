def GCD(n,m):
    if(int(n)!=n or int(m)!=m):
        return "ERROR";
    m = abs(m); n = abs(n);
    m = max(n,m);
    n = min(n,m);
    if(n==0):
        return m;
    return GCD(m%n,n);

print(GCD(36,123)) # 123,36
print(GCD(12,30))
print(GCD(-24,30))
print(GCD(48,1.8))