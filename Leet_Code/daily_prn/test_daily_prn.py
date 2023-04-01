# def gcd(a, b) :
#      if b == 0 :
#           return a
#      else :
#           return gcd(b, a % b)

# a, b = [abs(int(item)) for item in(input("Enter Input : ").split(" "))]
# if a < b:
#      a, b = b, a
# if a == 0 and b == 0 :
#      print("Error! must be not all zero.")
# else :
#      ans = gcd(a,b)
#      print(f'The gcd of {a} and {b} is : {ans}'.format(a,b,ans))

def gcd(a,b):
     if(b == 0):
          return abs(a)
     else:
        return gcd(b, a % b)
    
a, b = [(int(item)) for item in(input("Enter Input : ").split(" "))]
if a < b:
     a, b = b, a
if a == 0 and b == 0 :
     print("Error! must be not all zero.")
else :
     ans = gcd(a,b)
     print(f'The gcd of {a} and {b} is : {ans}'.format(a,b,ans))

