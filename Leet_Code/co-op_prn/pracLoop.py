# https://www.programiz.com/python-programming/examples/pyramid-patterns?fbclid=IwAR1NeKoa9gsFqVXPIvZ4WfGG075pFDTQA48Li9-1TlaQUhDwwr84rNXRcQo

# ex5
# inp = int(input("input : "))
# for i in range(inp):
#     for j in range(inp-i):
#         print(j+1,end=' ')
#     print()

#ex6
# inp = int(input("input : "))
# for i in range(0,inp):
#     for j in range(0,inp-i):
#         print("  ",end='')
#     for j in range(i*2+1):
#         print("* ",end='')
#     print()

# ex7
inp = int(input("iput : "))
cnt = 0
for i in range(inp):
    for j in range(inp-i):
        print("  ",end="")
    for j in range((i*2)+1):

        if(j >((i*2)+1)//2):
            cnt -= 1    
        else:
            cnt += 1
        print(cnt,end=" ")
    print()

# ex8
# inp = int(input("iput : "))
# for i in range(0,inp):
#     for j in range(0,i):
#         print("  ",end='')
#     for j in range(0,(inp-1-i)*2+1):
#         print("* ",end='')
#     print()

# # ex9
# inp = int(input("input : "))
# for i in range(inp):
