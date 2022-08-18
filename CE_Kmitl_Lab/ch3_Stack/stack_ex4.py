class StackCalc:

    def __init__(self):
        self._data = [];
        self._resut = 0;
        self._size = 0;

    def push(self, data):
        self._data.append(data)
        self._size += 1

    def pop(self):
        if(self._size == 0):
            return"Can not pop"
        self._size -= 1
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def getData(self):
        return self._data

    def size(self):
        return self._size

    def isEmpty(self):
        if(self._size == 0):
            return True
        return False

    def getValue(self):
        return int(self._resut);

    def run(self, arg):
        # store,cal section
        opt = ["+", "-", "*", "/", "DUP", "POP", "PSH"];
        char_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
        for item in arg:
            if((item not in opt) and (item[0] not in char_num)):
                print("Invalid instruction: "+str(item));
                exit();
        #    self.push(item);
        # for item in self.getData():
        #     print("prn 44 -> "+item);
            num1 = 0;
            num2 = 0;
            # normal operator
            if(item in opt[0:4]):
                if(item == "+"):
                    num1 = int(self.pop());
                    num2 = int(self.pop());
                    self.push(num1+num2);
                elif(item == "-"):
                    num1 = int(self.pop());
                    num2 = int(self.pop());
                    self.push(num1-num2);
                elif(item == "*"):
                    num1 = int(self.pop());
                    num2 = int(self.pop());
                    self.push(num1*num2);
                elif(item=="/"):
                    num1 = int(self.pop());
                    num2 = int(self.pop());
                    self.push(num1/num2);
                continue;
            #extra operator
            if(item in opt[4:len(opt)]):
                if(item == "DUP"):
                    self.push(self._data[-1]);
                    # print("prn found DUP");
                elif(item == "POP"):
                    self.pop();
                    # print("prn found POP");
                elif(item == "PSH"):
                    pass;
                  
                continue;  
                
            #if not any operator then push to stack
            self.push(item);
        
        #end cal
        if(self.isEmpty()):
            self._resut = 0;
            return;
        self._resut = self.peek();
    
print("* Stack Calculator *");
arg = input("Enter arguments : ").split(" ");

machine = StackCalc();
machine.run(arg)
print(machine.getValue())
