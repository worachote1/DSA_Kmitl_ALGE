
print("*** Converting hh.mm.ss to seconds ***");
h, m, s = input("Enter hh mm ss : ").split()
h=int(h);
m=int(m);
s=int(s);
res = 3600*h+60*m+s;

if(h<0):
    print("hh(%d) is invalid!"%(h))
    exit();
elif(m>59 or m<0):
    print("mm(%d) is invalid!"%(m))
    exit();
elif(s>59 or s<0):
    print("ss(%d) is invalid!"%(s))
    exit();

if(h<10):
    h = "".join(["0",str(h)]);
if(m<10):
    m = "".join(["0",str(m)]);
if(s<10):
    s = "".join(["0",str(s)]);
print("%s:%s:%s = "%(h,m,s),end="");
print("{:,}".format(res),"seconds");
