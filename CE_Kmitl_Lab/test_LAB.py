r = ["wdw","bmw","daf"];
m = [1,2,3,4]
print(r);
ss = " ".join(r);
print(" ".join(str(item) for item in m));

t = [10,20,30]
ss = "500000"
print("{:,}".format(int("50000")))

closeData = {")":"(","]":"[","}":"{"}
for i in closeData:
    print(i);