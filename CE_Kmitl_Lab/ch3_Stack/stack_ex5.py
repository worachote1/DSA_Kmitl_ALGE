from inspect import stack
from pickle import STACK_GLOBAL


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

inp = input("Enter Input : ").split(",");
tree = Stack();
hight = [];
#print(inp);
for item in inp:
    if(item[0]=="A"):
        if(tree.isEmpty()):
            tree.push(item);
            hight.append(int(item[-1]));
            continue;
        if(int(item[-1])>int(tree.peek()[-1])):
            while(True):
                tree.pop();
                hight.pop();
                if(tree.isEmpty()):
                    break;
                if(int(item[-1])<=int(tree.peek()[-1])):
                    break;

            tree.push(item);
            hight.append(int(item[-1]));
            continue; 

        tree.push(item);
        hight.append(int(item[-1]));

    if(item=="B"):
        #clone temp
        temp_hight = [];
        for h in hight:
            temp_hight.append(h);
        
        print("now temp = ",temp_hight);

        if(len(temp_hight)==0):
            print(0);
            continue;
        if(len(temp_hight)==1):
            print(1);
            continue;
        while(temp_hight[-1]>temp_hight[-2]):

            temp_hight.pop();
            if(len(temp_hight)==1):
                break;
            
        print(len(temp_hight));
        

    if(item=="S"):
        for i in range(len(hight)):
            if(hight[i]%2==0):
                hight[i]-=1;
                continue;
            hight[i]+=2;
    

# prn bug : A 4,A 3,B