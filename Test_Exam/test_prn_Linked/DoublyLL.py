class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "linked list : "
        cur, s = self.head, "linked list : "
        for i in range(self.size()-1):
            s += str(cur.data) + "->"
            cur = cur.next
        s += cur.data
        return s

    def str_reverse(self):
        if self.isEmpty():
            return "reverse :"
        cur, s = self.head, "reverse : "
        while cur.next is not None:
            cur = cur.next
        for i in range(self.size()-1):
            s += str(cur.data) + "->"
            cur = cur.prev
        s += cur.data
        return s

    def isEmpty(self):
        return self.head is None

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = newNode
        newNode.prev = cur

    def size(self):
        cur, cnt = self.head, 0
        while cur is not None:
            cnt += 1
            cur = cur.next
        return cnt

    def add_before(self, data):
        newNode = Node(data)
        cur = self.head
        if self.isEmpty():
            self.head = newNode
            return
        cur.prev = newNode
        newNode.next = cur
        self.head = newNode
        return

    def insert(self, index, data):
        index = int(index)
        cur = self.head
        newNode = Node(data)
        if index < 0 or index > self.size():
            print("Data cannot be added")
            return
        print(f'index = {index} and data = {data}')
        if index == 0 and self.size() == 0:
            self.head = newNode
            return
        elif index == 0:
            cur.prev = newNode
            newNode.next = cur
            self.head = newNode
            return
        if index == self.size():
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode
            newNode.prev = cur
            return
        for i in range(index):
            cur = cur.next
        newNode.prev = cur.prev
        cur.prev.next = newNode
        cur.prev = newNode
        newNode.next = cur
        return

    def remove(self, data):
        if self.isEmpty():
            print("Not Found!")
            return
        cnt = 0
        cur = self.head
        while cur is not None:
            if cur.data == data:
                if cur.prev is None and cur.next is None:
                    self.head = None
                elif cur.prev is None and cur.next is not None:
                    self.head = cur.next
                    self.head.prev = None
                elif cur.prev is not None and cur.next is None:
                    cur.prev.next = None
                elif cur.prev is not None and cur.next is not None:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                print(f'removed : {data} from index : {cnt}')
                return
            cnt += 1
            cur = cur.next
        print("Not Found!")
        return


l = DoublyLinkedList()
inp = input("Enter Input : ").split(",")
for data in inp:
    task = data.strip().split(" ")
    if task[0] == "A":
        l.append(task[1])
    if task[0] == "Ab":
        l.add_before(task[1])
    if task[0] == "I":
        opr = task[1].split(":")
        l.insert(opr[0], opr[1])
    if task[0] == "R":
        l.remove(task[1])
    print(l)
    print(l.str_reverse())
