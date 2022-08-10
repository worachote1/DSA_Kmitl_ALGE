
x = int(input("Enter Input : "));
maxCol = (2*x+1)+3;
markIndex = (maxCol//2+1)-1;

# Top half
for i in range(x+2):
    for j in range(maxCol):
        # if it's top row
        if(i == 0):
            if(j <= x-i):
                print(".", end="");
            elif(j == x+1):
                print("#", end="");
            elif(j > x+1):
                print("+", end="");
        # if it's below row
        elif(i == (x+2)-1):
            if(j < maxCol//2):
                print("#", end="");
            elif(j >= maxCol//2):
                print("+", end="");
        # if it's between top and below row
        else:
            if((j >= maxCol//2-i-1 and j < maxCol//2)
            or (j > maxCol//2 and j < maxCol-1)):
                print("#", end="");

            elif(j < x-i+1):
                print(".", end="");

            else:
                print("+", end="");
    print();

# below half
for i in range(x+2):
    for j in range(maxCol):
        # if it's top row
        if(i == 0):
            if(j < maxCol//2):
                print("#", end="");
            elif(j >= maxCol//2):
                print("+", end="");

        # if it's below row
        elif(i == (x+2)-1):
            if(j<maxCol//2):
                print("#",end="");
            elif(j==maxCol//2):
                print("+",end="");
            else:
                print(".",end="");

        # if it's between top and below row
        else: 
            if(j==0 or j==maxCol//2-1):
                print("#",end="");
            elif((j>0 and j<maxCol//2-1) or (j>=maxCol//2 and j<maxCol-i)):
                print("+",end="");
            else:
                print(".",end="");

    print();