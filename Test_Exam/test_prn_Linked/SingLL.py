class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur = self.head
        s = str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        newNode = Node(item)
        if(self.head == None):
            self.head = newNode
            return
        # the move to tail
        cur = self.head
        while(cur.next != None):
            cur = cur.next
        cur.next = newNode

    def addHead(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    def search(self, item):
        cur = self.head
        if(cur == None):
            return "Not Found"
        while(cur != None):
            if(cur.value == item):
                return "Found"
            cur = cur.next
        return "Not Found"

    def index(self, item):
        cur = self.head
        if(cur == None):
            return -1
        index = 0
        while(cur != None):
            if(cur.value == item):
                return str(index)
            cur = cur.next
            index += 1
        return -1

    def size(self):
        cur = self.head
        size = 0
        while(cur != None):
            size += 1
            cur = cur.next
        return size

    def pop(self, pos):
        if(pos < 0):
            return "Out of Range"
        if(pos > self.size()-1):
            return "Out of Range"
        if(self.size() == 1):
            self.head = None
            return "Success"
        # move to element before pos
        cur = self.head
        posIdx = 0
        while(posIdx < pos-1):
            cur = cur.next
            posIdx += 1
        if(cur.next.next == None):
            cur.next = None
        elif(cur.next.next != None):
            cur.next = cur.next.next
        return "Success"
    # my prn test print

    def testDisplay(self):
        temp = self.head
        if(temp == None):
            print("LinkedList not exist")
            exit()
        while temp != None:
            print(temp.value)
            temp = temp.next


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1}".format(L.search(i[3:]), i[3:]), end="")
        print(' in {0}'.format(L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
