class Stack:
    
    def __init__(self):
        self._data = [];


    def push(self,data):
        self._data.append(data);


    def pop(self):
        return self._data.pop();

    def peek(self):
        return self._data[len(self._data)-1];

    def getData(self):
        return self._data;


test_stack = Stack();
test_stack.push(44);
test_stack.push(12);
test_stack.push(13);
test_stack.pop();
print(test_stack.getData());
print(test_stack.peek());