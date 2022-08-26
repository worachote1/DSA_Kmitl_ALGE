def mergeOverlappingIntervals(intervals):
    #sort all intervals
    a = intervals;
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if(a[j+1][0]<a[j][0]):
                temp = a[j+1];
                a[j+1] = a[j];
                a[j] = temp; 

    #merge all overlaping interval
    res = [];
    for start,end in a:
        if(len(res)==0):
            res.append([start,end]);
            continue;
        if(start>res[-1][1]):
            res.append([start,end]);
            continue;
        elif(start<=res[-1][1]):
            maxEnd = max(end,res[-1][1]);
            res[-1][1] = maxEnd;
    return res;

prn = [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
  ]

p11 = [
    [1, 22],
    [-20, 30]
]
print(mergeOverlappingIntervals(prn));
print(mergeOverlappingIntervals(p11));
