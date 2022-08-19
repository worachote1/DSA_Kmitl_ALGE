class Queue:
    def __init__(self):
        self.q = []
    def Enqueue(self,i):
        self.q.append(i)
    def Dequeue(self):
        if(len(self.q)==0):
            return ""
        return self.q.pop(0)
    def isEmpty(self):
        return len(self.q) == 0
    def size(self):
        return len(self.q)
    def show(self):
        return self.q.copy()

Shelf = Queue();
inp = input("Enter Input : ").split('/');
# print("[0] ->",inp[0].split(" "))
# print("[1] ->",inp[1].split(","))

orders = inp[1].split(",");
# 1 2 7 2 4 6 8/E 5,D,D,E 1,E 3,D
for book in inp[0].split(" "):
    Shelf.Enqueue(book);
    
# print("orders -> ",orders);
#use orders
for item in orders:
    if(item[0]=="D"):
        Shelf.Dequeue();
        continue;
    Shelf.Enqueue(item[2:]);


if(Shelf.size()==0 or Shelf.size()==1):
    print("NO Duplicate")
    exit();
#Chcek duplicate
count = 0;
for i in range(Shelf.size()-1):
  for j in range(i+1,Shelf.size()):
        if(Shelf.q[j]==Shelf.q[i]):
            print("Duplicate");
            exit();

print("NO Duplicate")

#sanfong method
# print(Shelf.q);
# for i in Shelf.q :
#     if(Shelf.q.count(i)>1):
#         print("Duplicate");
#         exit();
# print("NO Duplicate");        

# 1 1 1 1/E 2,E 3,D,D
