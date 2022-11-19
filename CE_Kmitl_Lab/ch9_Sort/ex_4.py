def sort_bubble(data : list):
    for i in range(len(data)):
        for j in range(len(data)-1-i):
            if(data[j]>data[j+1]):
                temp = data[j]
                data[j]=data[j+1]
                data[j+1]=temp
def find_med(data : list):
    n = len(data)
    sort_bubble(data)
    if(n%2!=0):
        return data[n//2]
    else:
        return (data[(n//2)-1] + data[n//2]) / 2


l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    for i in range(len(l)):
        data = [l[i] for i in range(0,i+1)]
        ss = "list = {0} : ".format(data)
        med = find_med(data)
        format_med = "{:.1f}".format(med)
        ss = ss+"median = {0}".format(format_med)
        print(ss)