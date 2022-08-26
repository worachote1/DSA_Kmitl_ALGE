def arrayOfProducts(array):
    res = [];
    for i in range(len(array)):
        p = 1;
        for j in range(len(array)):
            if(j==i):
                continue;
            p *= array[j];
        res.append(p);
    
    return res;

print(arrayOfProducts([5, 1, 4, 2]));