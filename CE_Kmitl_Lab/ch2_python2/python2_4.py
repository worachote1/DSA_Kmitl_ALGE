def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]
 
# wrapper function
def subsets_of_given_size(numbers, n):
    return [x for x in subsets(numbers) if len(x)==n]


x = input("Enter Your List : ").split(" ");
if(len(x)<=2):
    print("Array Input Length Must More Than 2");
    exit();

for i in range(len(x)):
    x[i]=int(x[i]);

res = [];

for i in reversed(range(0,len(subsets_of_given_size(x,3)))):
    sum = 0;
    #res_item = [];
    for j in range(3):
        sum += subsets_of_given_size(x,3)[i][j];
    if(sum==0):
        if(subsets_of_given_size(x,3)[i] not in res):
            res.append(subsets_of_given_size(x,3)[i]); 

print(res);
# print("prn-------------");
# print(subsets_of_given_size(x,3));
# -25 44 11 23