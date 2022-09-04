from sys import maxsize


def staircaseTraversal(height, maxSteps):
    
    if(height<=1):
        return 1;
    
    res_AllWays = 0;
    for i in range(1,min(maxSteps,height)+1):
        res_AllWays += staircaseTraversal(height-i,maxSteps);
    
    return res_AllWays;

print(staircaseTraversal(3,2));
print(staircaseTraversal(4,2));
print(staircaseTraversal(3,3));
print(staircaseTraversal(3,5));
print(staircaseTraversal(4,3));
print(staircaseTraversal(4,1));