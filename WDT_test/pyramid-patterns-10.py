# Example 10: Floyd's Triangle
'''
1
2 3
4 5 6
7 8 9 10
'''

# use: 1 min
num = 1
for i in range(1,4+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()