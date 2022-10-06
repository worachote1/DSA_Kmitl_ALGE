def harmonic_sum(n,sum=0):
    if(n==1):
        print(str(1)+" ",end="")
        return 1
    
    sum += 1/n + harmonic_sum(n-1)
    # print("1/",end="")
    # print(n)
    print('+ 1/{0} '.format(n),end="")
    return sum

print("= "+str(harmonic_sum(5)))