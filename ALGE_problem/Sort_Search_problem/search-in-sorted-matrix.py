def searchInSortedMatrix(matrix, target):
    # Write your code here.
    row = 0
    col = len(matrix[0])-1
    while((row >=0 and row < len(matrix)) and (col >= 0 and col < len(matrix[0]))):
        if(matrix[row][col]>target):
            col -= 1
        if(matrix[row][col]<target):
            row += 1
        elif(matrix[row][col]==target):
            return [row,col]
    return [-1,-1]