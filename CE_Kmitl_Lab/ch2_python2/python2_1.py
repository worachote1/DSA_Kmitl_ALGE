class Calculator :
    
    ### Enter Your Code Here ###
    def __init__(self, a):
        self.a = a;
    
    def __add__(self,b):
        ###Enter Your Code For Add Number###
        
        return self.a+b

    def __sub__(self,b):
        
        ###Enter Your Code For Sub Number### 
       
        return self.a-b

    def __mul__(self,b):

        ###Enter Your Code For Mul Number###
       
        return self.a*b

    def __truediv__(self,b):

        ###Enter Your Code For Div Number###
        
        return self.a/b

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x.__add__(y.a),x.__sub__(y.a),x.__mul__(y.a),x.__truediv__(y.a),sep = "\n")
