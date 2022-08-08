# Write a recursive function called flatten 
# which accepts an array of arrays 
# and returns a new array with all values flattened.


def flatten(arr):
    
    result_arr = [];
    for a in arr :
        if(type(a) is list):
            result_arr.extend(flatten(a));
        else:
            result_arr.append(a);

    return result_arr;

print(flatten([1, 2, 3, [4, 5]])); # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])); # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])); # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]));# [1, 2, 3]

result_arr = [];
b = [44];
c=5;
result_arr.append(b);
#result_arr.append(c);
#result_arr.extend(b);
print(result_arr);
#print(type(result_arr));
