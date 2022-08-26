def firstDuplicateValue(array):
    same = [];
    i = 0;
    for i in range(len(array)):
        if(array[i] not in same):
            same.append(array[i]);
            continue;
        return array[i];

    return -1;

print(firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]));
print(firstDuplicateValue([3, 1, 3, 1, 1, 4, 4]));
print(firstDuplicateValue([2, 1, 5, 3, 3, 2, 4]));
print(firstDuplicateValue([2, 1, 1]));