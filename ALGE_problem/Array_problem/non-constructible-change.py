def nonConstructibleChange(coins):
    res = 0;
    coins.sort();
    #print("coins -> ",coins);
    if(len(coins)==1):
        if(coins[0]==1):
            return 2;
        return 1;
    for i in range(len(coins)):
        
        if(coins[i]>res+1):
            return res+1;
        res += coins[i];

    return res+1;

print(nonConstructibleChange([1,1]));
print(nonConstructibleChange([1, 2, 3, 4, 5, 6, 7]));
print(nonConstructibleChange([1,1,4]));