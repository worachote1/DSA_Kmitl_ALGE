def zigzagTraverse(array):
    maxWidth = len(array[0])-1;
    maxHight = len(array)-1;

    res = [];
    row = 0;
    col = 0;
    goDown = True;
    while(not(row > maxHight or col > maxWidth)):
        res.append(array[row][col]);
        print("element b4 -> ",array[row][col],"and goDown : ",goDown);
        if(goDown):
            #if it hit border left or bottom
            if(row==maxHight or col==0):
                #hit border bottom
                if(row==maxHight):
                    col+=1;
                #hit border left
                elif(col==0):
                    row+=1;
                
                goDown=False;
            
            #if not hit any corner while goDown is True
            #then move down diagonal 
            else:
                row+=1;
                col-=1;
        
        elif(not goDown):
            #if it hit border right or top
            if(row==0 or col == maxWidth):
                #hit border right
                if(col==maxWidth):
                    row+=1;
                #hit border top
                elif(row==0):
                    col+=1;
                
                goDown=True;
            
            #if not hit any corner while goDown is True
            #then move up diagonal 
            else:
                row-=1;
                col+=1;

        print("row -> ",row," col -> ",col);
    return res;

# arr= [
#     [1, 3, 4, 10],
#     [2, 5, 9, 11],
#     [6, 8, 12, 15],
#     [7, 13, 14, 16]
# ]
# arr2 = [[1,3,4,10],[2,5,9,11]]
# print(zigzagTraverse(arr));    
# print("prn test mul -> ",len(arr)*len(arr[0]));
# print(zigzagTraverse(arr2));
# print("prn arr7 ");
# arr7= [
#     [1, 3, 4, 10, 11],
#     [2, 5, 9, 12, 19],
#     [6, 8, 13, 18, 20],
#     [7, 14, 17, 21, 24],
#     [15, 16, 22, 23, 25]
# ];
# print(zigzagTraverse(arr7));

# print("-------------")
# arr5 = [[1, 3],
#     [2, 4],
#     [5, 7],
#     [6, 8],
#     [9, 10]];
# print(zigzagTraverse(arr5));
print("arr 5");
arr5 =  [
    [1, 3],
    [2, 4],
    [5, 7],
    [6, 8],
    [9, 10]
];
print(zigzagTraverse(arr5));