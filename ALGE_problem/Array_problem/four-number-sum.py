
from traceback import print_tb


def fourNumberSum(array, targetSum):
    
    res =  [];
    data = dict();
    for i in range(len(array)-1):
        # print("prn -> ",array[i]);
        for j in range(i+1,len(array)):
            sumOfPair = array[i]+array[j];
            diff = targetSum - sumOfPair;
            if(diff in data):
                print("that diff = ",diff);
                for item in data[diff]:
                    print("SD");
                    res.append(item+[array[i],array[j]]);
                    print("res -> ",res);

        for j in range(0,i):
            sumOfPair = array[i]+array[j];
            print("sum of pair -> ",sumOfPair);
            if(sumOfPair not in data.keys()):
                data[sumOfPair]=[[array[j],array[i]]];
            else:
                data[sumOfPair].append([array[j],array[i]]);

        print("prn data -> ",data)
    return res;

array = [7, 6, 4, -1, 1, 2];
print(fourNumberSum(array,16));