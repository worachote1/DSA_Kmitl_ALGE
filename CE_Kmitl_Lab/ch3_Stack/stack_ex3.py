class Stack:
    # __ 
    def __init__(self):
        self._data = [];
        self._size = 0;


    def push(self,data):
        self._data.append(data);
        self._size+=1;

    def pop(self):
        if(self._size==0):
            return"Can not pop";
        self._size-=1;
        return self._data.pop();

    def peek(self):
        return self._data[-1];

    def getData(self):
        return self._data;

    def size(self):
        return self._size;

    def isEmpty(self):
        if(self._size==0):
            return True;
        return False;

    def items(self):
        return self._data;
#prn main
# K+L-M*N+(O^P)*W/U/V*T+Q
inp = input('Enter Infix : ')
S = Stack()
result = "";
#cal section
#operator presence
# 1) (),{},[]
# 2) ^   : R->L
# 3) *,/ : L->R
# 4) +,- : L->R
opt = {"+":1,"-":1,"*":2,"/":2,"^":3};
for item in inp:
      
    if(item not in opt and not item in["(",")"]):
        result += item;
        continue;

    if(item == "("):
        S.push(item);
        continue;
    if(item == ")"):
        prn_pop = S.pop();
        while(prn_pop!="("):
            result+=prn_pop;
            prn_pop = S.pop();

        continue;

    #if it's operater
    while(True):
        if(S.isEmpty() or S.peek()=="("):
            S.push(item);
            break;            

        if(opt.get(item)>opt.get(S.peek())):
            S.push(item);
            break;
        elif(opt.get(item)<=opt.get(S.peek())):
            result += S.pop();
  
#end loop for in
#a*b+c -> test error ?
print('Postfix : ', end='');
print(result,end="");
while not S.isEmpty():
    print(S.pop(), end='');
print()