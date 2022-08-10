
print("*** Converting hh.mm.ss to seconds ***");
h, m, s = input("Enter hh mm ss :").split()
h=int(h);
m=int(m);
s=int(s);
res = 3600*h+60*m+s;
print(h,":",m,":",s," = ","{:,}".format(res),"seconds");
