s = ['K', 'M', 'I', 'T', 'L', 'C', 'o', '2', '5', '6', '3'];
prn = ''.join([str(elem) for elem in s]); #array to string
print(prn);
print(prn[len(prn)-2:])
print(s);

opt = ["+","-","*","/","^"];
print(opt[0:2]);
print(opt[2:4]);
print(opt[-1]);

my_dict = {"+":1,"-":1,"*":2,"/":2,"^":3};
print(my_dict)
for item in my_dict:
    print(item);
print(my_dict.get('-'));
