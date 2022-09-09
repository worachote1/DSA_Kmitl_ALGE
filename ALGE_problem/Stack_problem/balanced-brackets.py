class Stack():
    def __init__(self):
        self.arr = [];
    
    def size(self):
        return len(self.arr);

    def push(self,i):
        self.arr.append(i);
    def pop(self):
        self.arr.pop();
    def peek(self):
        return self.arr[-1];
    def isEmpty(self):
        return len(self.arr)==0;

        
def balancedBrackets(string):
    # Write your code here.
    play  = Stack();
    openData = ["(","[","{"];
    closeData = {")":"(","]":"[","}":"{"};
    for item in string:
        if(item in openData):
            play.push(item);
        elif(item in closeData):
            #print("play -> ",play.peek()," | all -> ",play.arr);
            if(play.isEmpty()):
                return False;
            else:
                if(closeData[item]==play.peek()):
                    play.pop();
                    continue;
                return False;
                

    if(play.isEmpty()):
        return True     
    return False;
        

print(balancedBrackets("([])(){}(())()()"))
print(balancedBrackets( "()[]{}{"));