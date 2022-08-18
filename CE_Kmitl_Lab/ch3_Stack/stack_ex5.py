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
        return self._data[-1]

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


inp = input("Enter Input : ").split(",")
tree = Stack()
hight = []
# print(inp);
for item in inp:
    if(item[0] == "A"):
        if(tree.isEmpty()):
            tree.push(item)
            hight.append(int(item[1:]))
            continue

        tree.push(item)
        hight.append(int(item[1:]))

    if(item == "B"):
        # clone temp
        temp_hight = []
        for h in hight:
            temp_hight.append(h)
        #print("now temp = ", temp_hight)
        count = 0
        if(len(temp_hight) == 1):
            count += 1
        else:
            for i in range(len(temp_hight)-1, 0-1, -1):
                temp_hight_2 = []
                if(i == len(temp_hight)-1):
                    count += 1
                    # print("first prn "+str(i)+" which is : "+str(temp_hight[i]));
                    continue
                passCheck = temp_hight[i+1:]
                # print(passCheck);
                check = True
                for j in passCheck:
                    if(temp_hight[i] <= j):
                        check = False
                        break
                # count+=1;
                if(check):
                    count += 1
                    # print("prn "+str(i)+" which is : "+str(temp_hight[i]));

        print(count)

    if(item=="S"):
        for i in range(len(hight)):
            if(hight[i]%2==0):
                hight[i]-=1;
                continue;
            hight[i]+=2;


# prn bug : A 4,A 3,B
