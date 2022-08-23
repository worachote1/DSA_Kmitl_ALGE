def isValidSubsequence(array, sequence):
    posSub_array = 0;
    for i in range(len(array)):
        if(sequence[posSub_array]==array[i]):
            posSub_array+=1;
        if(posSub_array==len(sequence)):
            return True;

    return False;

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[5, 1, 22, 25, 6, -1, 8, 10]));
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[22, 25, 6]));
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[5, -1, 8, 10]));
print(isValidSubsequence([1, 1, 1, 1, 1],[1, 1, 1]));
print(isValidSubsequence([1, 1, 6, 1],[1, 1, 1, 6]));