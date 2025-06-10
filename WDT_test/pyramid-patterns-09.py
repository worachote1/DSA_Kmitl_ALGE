# Example 9: Pascal's Triangle
'''
           1
         1   1
       1   2   1
     1   3   3    1
   1  4    6   4   1
 1  5   10   10  5   1
'''

# use: 13 min

row = 6
pascal_arr = [[0 for j in range(row*2)] for i in range(row*2)]
for i in range(row):
  temp_Idx = 0
  for j in range(row-i):
    print(' ',end='')
    temp_Idx += 1 
  for j in range(i+1):
    if(j == 0 or j==i or i == 0):
      pascal_arr[i][temp_Idx] = 1
      print(pascal_arr[i][temp_Idx], end=' ')
    else:
      pascal_arr[i][temp_Idx] = pascal_arr[i-1][temp_Idx] + pascal_arr[i-1][temp_Idx+1] 
      print(pascal_arr[i][temp_Idx], end='  ')
    temp_Idx += 1
  print()