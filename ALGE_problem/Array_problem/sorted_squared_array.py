def sortedSquaredArray(array):
    res = [];
    for item in array:
        res.append(item*item);
    if(res != []):
        res.sort();
        return res;
    return []

