# Example 7: Full Pyramid of Numbers
'''
        1 
      2 3 2 
    3 4 5 4 3 
  4 5 6 7 6 5 4 
5 6 7 8 9 8 7 6 5
'''

# use: 7 min
# use: min
for i in range(1, 5+1):
    for j in range(5-i):
        print('  ',end='')

    for j in range(i, i*2-1):
        print(j, end=' ')
    
    for j in range(i*2-1, i-1, -1):
        print(j, end=' ')
    
    print()