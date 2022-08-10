import itertools


print("*** Fun with Drawing ***");
x=int(input("Enter input : "));

# print("input 2 -> lenX = ",len(".*.*."));
# print("input 5 -> lenX = ",len("....*.......*...."));
# print("input 7 -> lenX = ",len("......*...........*......"));

maxCol = x*3+(x-3);
#top half
for i in range(x):
    # j==maxCol-x+i
    for j in range(maxCol):
        #left side
        if(j==x-i-1 or j== x-i-1+2*i
        or j==(maxCol)-x-i or j==((maxCol)-x-i)+(2*i)):
            print("*",end="");
        elif((j>x-i-1 and j< x-i-1+2*i)
        or (j>(maxCol)-x-i and j<((maxCol)-x-i)+(2*i))):
            print("+",end="");  
        else:
            print(".",end="");
  
    print();


#below half
for i in range(x*2-2):
    for j in range(maxCol):
        if(j==i+1 or j==(maxCol-1)-i-1):
            print("*",end="");
        elif(j>i+1 and j<(maxCol-1)-i-1):
            print("+",end="");
        else:
            print(".",end="");
    print();

