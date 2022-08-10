def capitalizeWords(arr):
    res = [];
    if(len(arr)==0):
        return res;
    res.append(arr[0].upper());
    return res + capitalizeWords(arr[1:]);

words = ['i', 'am', 'learning', 'recursion']

#print(capitalizeWords(words));  # ['I', 'AM', 'LEARNING', 'RECURSION']
