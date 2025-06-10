# Example 3: Program to print half pyramid using alphabets
'''
A
B B
C C C
D D D D
E E E E E
'''
# use: 3 min..
for i in range(5):
    for j in range(i+1):
        print(chr(65+i), end=' ')
    print()