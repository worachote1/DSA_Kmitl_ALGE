class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,size,maxcol):
        self.table = [None]*size
        self.size = size
        self.maxcol = maxcol

    def insert(self,key,value):
        idx = 0
        if not self.isFull():
            for i in key:
                idx += ord(i) % self.size
            idx %= self.size

            if self.table[idx] is None:
                self.table[idx] = Data(key,value)
            
            elif self.table[idx] is not None:
                r, newidx = 0, idx
                print(f'collision number {r+1} at {newidx}')
                
                while self.table[newidx] is not None :
                    r += 1
                    newidx = ( idx + r * r ) % self.size
                    if self.table[newidx] is None:
                        self.table[newidx] = Data(key,value)
                        break
                    if self.maxcol <= r:
                        print("Max of collisionChain")
                        break
                    print(f'collision number {r+1} at {newidx}')

    def isFull(self):
        return None not in self.table
    
    def __str__(self):
        s = ""
        for i in range(len(self.table)):
            s += f'#{i+1}      {self.table[i]}\n'
        return s

print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split("/")
size, maxcol = inp[0].split()
data = inp[1].split(",")
Hash = hash(int(size),int(maxcol))
for i in data:
    Hash.insert(i.split()[0],i.split()[1])
    print(Hash,end="")
    print("---------------------------")
    if Hash.isFull():
        print("This table is full !!!!!!")
        break