from queue import Queue
class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;

class Queue:
    def __init__(self):
        #Queue is empty
        self.front = None;
        self.rear = None;
        
    def isEmpty(self):
        return self.front == None;
    
    def Enqueue(self,data):
        temp = Node(data);

        if self.rear == None:
            self.front = self.rear = temp;

        else :   
            self.rear.next = temp;
            self.rear = temp;

    def display(self):
        temp = self.front;
        while temp is not None:
            print(temp.data);
            temp = temp.next;


q = Queue();
q.Enqueue(44);
q.Enqueue(12);
q.Enqueue(54);
q.Enqueue(39);
q.Enqueue(62);
q.display();

