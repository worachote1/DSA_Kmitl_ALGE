# def powerset(array):
#     subsets = [[]]
#     for i in array:
#         for j in range(len(subsets)):
#             cur = subsets[j]
#             subsets.append(cur+[i])

#     return subsets
    
# def powerset(array):
#     subsets = [[]]
#     for i in array:
#         for j in range(len(subsets)):
#             cur = subsets[j]
#             subsets.append(cur+[i])

#     return subsets

# arr = [1,2,3]
# print(powerset(arr))

a = [[]]
b = a[0] + []
print(b) 