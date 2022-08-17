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
        return self._data[len(self._data)-1];

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
print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:
    s.push(e)

print(s.size(),"Data in stack : ",s.items())

while not s.isEmpty():
    s.pop()
    
print(s.size(),"Data in stack : ",s.items())
#K M I T L C E 2 5 6 3


