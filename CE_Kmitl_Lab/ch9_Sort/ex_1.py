def bubbleSort(ar):   
    # Base Case: If array
    # contains a single element
    if len(ar) <= 1:
        return ar
    # Base Case: If array
    # contains two elements
    if len(ar) == 2:
        return ar if ar[0] < ar[1] else [ar[1], ar[0]]
    # Store the first two elements
    # of the list in variables a and b
    a, b = ar[0], ar[1]
    # Store remaining elements
    # in the list bs
    bs = ar[2:]
    # Store the list after
    # each recursive call
    res = [] 
    if a < b:
        res = [a] + bubbleSort([b] + bs)       
    else:
        res = [b] + bubbleSort([a] + bs)     
    return bubbleSort(res[:-1]) + res[-1:]

inp = list(map(int, input("Enter Input : ").split()))
print(bubbleSort(inp))