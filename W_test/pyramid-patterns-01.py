# Example 1: Program to print half pyramid using *
'''
*
* *
* * *
* * * *
* * * * *
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print('')