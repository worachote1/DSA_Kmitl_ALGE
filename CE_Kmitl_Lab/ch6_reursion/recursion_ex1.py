def fac(num):
    if(num == 0 or num == 1):
        return 1;
    return num*fac(num-1);

num = int(input("Enter Number : "));
print('{0}! = {1}'.format(num,fac(num)));
