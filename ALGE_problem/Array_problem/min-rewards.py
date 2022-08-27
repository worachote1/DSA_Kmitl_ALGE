from xml.sax.handler import property_interning_dict


def minRewards(scores):

    a = [0 for i in range(len(scores))];
    
    for i in range(len(scores)):
        if(i==0):
            a[i]+=1;
            continue;
        
        k=i;
        a[i]+=1;
        #if left-adjacent have higher score
        if(scores[k]<scores[k-1]):
            while(k>0):
                if(scores[k]<scores[k-1] and a[k-1]<=a[k]):
                    maxVal = max(a[k-1],a[k]+1);
                    a[k-1]=maxVal;
                    k-=1;
                else:
                    break;
        
        #if left-adjacent have lower score
        elif(scores[k]>=scores[k-1]):
            maxVal = max(a[k],a[k-1]+1);
            a[k]=maxVal;

    print(a);

    return sum(a);

scores = [8, 4, 2, 1, 3, 6, 7, 9, 5];
a = [0 for i in range(10)];
print(minRewards(scores));
print("test case 8 ");
scores_8 = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9];
print(minRewards(scores_8));