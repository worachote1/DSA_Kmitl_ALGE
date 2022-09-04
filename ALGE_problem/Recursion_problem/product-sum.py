def productSum(array,multiplier=1):
    sum  = 0;
    for item in array:
        if(type(item) is int):
            sum += item;
        elif(type(item) is list):
            sum += productSum(item,multiplier+1);

    return sum*multiplier;

array =  [5, 2, [7, -1], 3, [6, [-13, 8], 4]];

print(productSum(array));