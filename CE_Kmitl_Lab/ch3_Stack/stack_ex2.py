class Stack:
    # __
    def __init__(self):
        self._data = []
        self._size = 0

    def push(self, data):
        self._data.append(data)
        self._size += 1

    def pop(self):
        if(self._size == 0):
            return"Can not pop"
        self._size -= 1
        return self._data.pop()

    def peek(self):
        return self._data[len(self._data)-1]

    def getData(self):
        return self._data

    def size(self):
        return self._size

    def isEmpty(self):
        if(self._size == 0):
            return True
        return False

    def items(self):
        return self._data


s = Stack()
ls = input("Enter expresion : ")
lsToString = ''.join([str(elem) for elem in ls])

# check unmatch
# (a+c)(a-b)*c(-a
count = 0
index_lastPush = -99
close_arr = [']', ')', "}"]
for item in ls:
    count += 1
    if(item in ['[', '(', '{']):
        s.push(item)

    else:
        # close_arr = [']',')',"}"];
        if(item in close_arr):
            temp = s.pop()
            if(temp == '['):
                if(item != ']'):
                    print(lsToString+" Unmatch open-close")
                    exit()
                else:
                    index_lastPush = count-1
            if(temp == '('):
                if(item != ')'):
                    print(lsToString+" Unmatch open-close")
                    exit()
                else:
                    index_lastPush = count-1
            if(temp == '{'):
                if(item != '}'):
                    print(lsToString+" Unmatch open-close")
                    exit()
                else:
                    index_lastPush = count-1

# print("test size ",s.size());
# check section
# print("test index ", index_lastPush)
if(s.isEmpty()):
    # check excess close
    for prn in ls[index_lastPush+1:]:
        if(prn in close_arr):
            print(lsToString+" close paren excess");
            exit();   
    # it's Match
    print(lsToString+" MATCH")
    exit()

# excess open
restToString = ''.join([str(elem) for elem in s.items()])
# if s.items()[0] in ['[','(','{']
print(lsToString+" open paren excess   "+str(s.size())+" : "+restToString)


# check excess close
# print(lsToString+" close paren excess");

# (a+c)(a-b)*c(-a

# print("prn");
# print(s.items());

# check bracket
