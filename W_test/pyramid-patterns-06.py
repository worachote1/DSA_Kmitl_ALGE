# Example 6: Program to print full pyramid using *
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

'''

# use: 4 min
# use: 4 min

for i in range(5):
    for j in range(5-i-1):
      print('  ', end='')
    for j in range(((i+1)*2)-1):
       print('* ',end='')
    print()