class Node:
    def __init__(self,v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node("|")

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next is not None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        cur, cnt = self.head, 0
        while cur is not None:
            cnt += 1
            cur = cur.next
        return cnt

    def insert(self,item):
        newNode = Node(item)
        if self.size() == 1:
            self.head = newNode
            self.head.next = Node("|")
        else:
            cur = self.head
            prev = None
            while cur.value != "|":
                prev = cur
                cur = cur.next
            prev.next = newNode
            newNode.next = cur

    def left(self):
        cur = self.head
        prev = None
        
        if cur.value == "|":
            return 
        while cur.next.value != "|":
            prev = cur
            cur = cur.next
        if prev is None:
            self.head = Node("|")
            self.head.next = cur
        else:
            newNode = Node("|")
            prev.next = newNode
            newNode.next = cur

        if cur.next.next is not None:
            cur.next = cur.next.next
        else:
            cur.next = None

    def right(self):
        newNode = Node("|")
        cur = self.head
        prev = None
        while cur.value != "|":
            prev = cur
            cur = cur.next
        if cur.next is None:
            return 
        
        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next
        
        if cur.next.next is not None:
            newNode.next = cur.next.next
            cur.next.next = newNode
        else:
            newNode.next = None
            cur.next.next = newNode

    def backspace(self):
        newNode = Node("|")
        cur = self.head
        prev = None
        
        if cur.value == "|":
            return 
        while cur.next.value != "|":
            prev = cur
            cur = cur.next
        if prev is None:
            self.head = newNode
        else:
            prev.next = newNode

        if cur.next.next is not None:
            newNode.next = cur.next.next
        else:
            newNode.next = None

    def delete(self):
        newNode = Node("|")
        cur = self.head
        prev = None
        while cur.value != "|":
            prev = cur
            cur = cur.next
        if cur.next is None:
            return 
        
        if prev is None:
            self.head = newNode
        else:
            prev.next = newNode
        
        if cur.next.next is not None:
            newNode.next = cur.next.next
        else:
            newNode.next = None


l = LinkedList()
inp = input("Enter Input : ").split(",")
for data in inp:
    task = data.split(" ")
    if task[0] == "I":
        l.insert(task[1])
    if task[0] == "L":
        l.left()
    if task[0] == "R":
        l.right()
    if task[0] == "B":
        l.backspace()
    if task[0] == "D":
        l.delete()
print(l)