# 1 1 1 1/E 2,E 3,D,D

# arr = ["P","R","H","T","J","V"];
arr = "PRHTJV"
for i in range(len(arr)//2):
    temp = arr[i];
    arr[i]="".join(arr[len(arr)-1-i]);
    arr[len(arr)-1-i] = temp;
    print(arr[i])
    print("asc");

print("prn reverse -> ",arr);