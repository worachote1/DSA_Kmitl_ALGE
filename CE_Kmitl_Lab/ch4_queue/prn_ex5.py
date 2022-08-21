class Stack:
    
    def __init__(self):
        self.items = []

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()
        
    def top(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def reverse(self):
        self.items.reverse()
    
    def __str__(self):
        return "".join(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def push_back(self,i):
        self.items.append(i)
    
    def pop(self):
        front = self.items[0]
        self.items = self.items[1:]
        return front

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def reverse(self):
        self.items.reverse()
    
    def __str__(self):
        return "".join(self.items)


inp = input("Enter Input (Normal, Mirror) : ").split(" ")
nor, mir = inp[0], inp[1]
mir = mir[::-1]
mir_boom = 0

mir_s = Stack()
mir_boom_q = Queue()

for data in mir:
    if mir_s.size() < 2:
        mir_s.push(data)
    else:
        mir_s.push(data)
        th, sc, fr = mir_s.pop(), mir_s.pop(), mir_s.pop()
        if not fr == sc == th:
            mir_s.push(fr)
            mir_s.push(sc)
            mir_s.push(th)
        else:
            mir_boom_q.push_back(fr)
            mir_boom += 1;

nor_s = Stack()
fail = 0
nor_boom = 0
cnt = 0

for data in nor:
    if nor_s.size() < 2:
        if nor_s.size() == 1 and data == nor_s.top():
            cnt = 2
        else:
            cnt = 0
        nor_s.push(data)
            
    elif cnt == 2 and not mir_boom_q.isEmpty():
        cnt = 0
        front = mir_boom_q.pop()
        nor_s.push(front)

        th, sc, fr = nor_s.pop(), nor_s.pop(), nor_s.pop()
        if fr == sc == th:
            fail += 1
        else:
            nor_s.push(fr)
            nor_s.push(sc)
            nor_s.push(th)
        nor_s.push(data)
    else:
        if data == nor_s.top():
            cnt = 2
        else:
            cnt = 0
        nor_s.push(data)
        th, sc, fr = nor_s.pop(), nor_s.pop(), nor_s.pop()
        if fr == sc == th:
            nor_boom += 1
        else:
            nor_s.push(fr)
            nor_s.push(sc)
            nor_s.push(th)

print("NORMAL :")
print(f'{nor_s.size()}')
nor_s.reverse()
if nor_s.size() == 0:
    print("Empty")
else:
    print(nor_s)
print(f'{nor_boom} Explosive(s) ! ! ! (NORMAL)')
if fail > 0:
    print(f'Failed Interrupted {fail} Bomb(s)')

print("------------MIRROR------------")

print(": RORRIM")
print(f'{mir_s.size()}')
mir_s.reverse()
if mir_s.size() == 0:
    print("ytpmE")
else:
    print(mir_s)
print(f'(RORRIM) ! ! ! (s)evisolpxE {mir_boom}')