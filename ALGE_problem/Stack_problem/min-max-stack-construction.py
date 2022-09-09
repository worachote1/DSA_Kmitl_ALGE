# Feel free to add new properties and methods to the class.
import sys;
class MinMaxStack:
    def __init__(self):
        self.arr = [];
        self.minMax_Data = [];
    def peek(self):
        return self.arr[-1];

    def pop(self):
        self.minMax_Data.pop();
        return self.arr.pop();

    def push(self, number):
        newData = {"min" : number ,"max" : number};
        if(self.size() > 0):
            last_minMax = self.minMax_Data[-1];
            newData["min"] = min(last_minMax["min"],number);
            newData["max"] = max(last_minMax["max"],number);
        
        self.minMax_Data.append(newData);
        self.arr.append(number);

    def size(self):
        return len(self.arr);

    def getMin(self):
        return self.minMax_Data[-1]["min"];

    def getMax(self):
        # Write your code here.
        return self.minMax_Data[-1]["max"];


# minMax = MinMaxStack();
