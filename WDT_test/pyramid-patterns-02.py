# Example 2: Program to print half pyramid a using numbers
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
# use: 56 sec...
for i in range(5):
    for j in range(i+1):
        print(j+1, end=' ')
    print()