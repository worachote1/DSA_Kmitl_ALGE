# Example 8: Inverted full pyramid of *
'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
# use: 4 min
# use: 2 min

for i in range(5, 0, -1):
    for j in range(5-i):
        print("  ",end='')

    for j in range(2*i-1):
        print("* ",end='')

    print()

#---------------------------------

# for i in range(1,5+1):
#     for j in range(i):
#       print("  ", end='')
    
#     for j in range(2*(5-i)-1):
#       print("* ", end='')
    
#     print()