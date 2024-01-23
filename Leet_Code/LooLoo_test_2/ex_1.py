def count_rectangles (coordinates, min_area):
    	#Write your code here
        result = 0
        sameYAxisData = {}
        for item in coordinates:
            if(item[0] not in sameYAxisData):
                sameYAxisData[item[0]] = [item]
            else:
                sameYAxisData[item[0]].append(item)
        
        # print("old dict data")
        # print(sameYAxisData)
        # sort data by second index
        for item in sameYAxisData.values():
            for i in range(len(item)-1):
                if(item[i][1] > item[i+1][1]):
                    temp = item[i][1]
                    item[i][1] = item[i+1][1]
                    item[i+1][1] = temp
        # print("new dict data")
        # print(sameYAxisData)
        
        listAxisData = []
        for item in sameYAxisData.values():
            listAxisData.append(item)
        # sort List data
        # print(listAxisData)
        for i in range(len(listAxisData)-1):
            for j in range(len(listAxisData)-1-i):
                if(listAxisData[j][0][0] > listAxisData[j+1][0][0]):
                    temp = listAxisData[j]
                    listAxisData[j] = listAxisData[j+1]
                    listAxisData[j+1] = temp

        # print(listAxisData)
        # find possible rect
        for i in range(len(listAxisData)):
            if(len(listAxisData[i]) < 2):
                continue
            for j in range(i+1,len(listAxisData)):
                # if(j == i):
                #     continue
                if(len(listAxisData[j]) < 2):
                    continue
                # print("vv")
                # print(listAxisData[i])
                # print(listAxisData[j])

                xLengthTop = listAxisData[j][1][0] - listAxisData[i][1][0]
                yLength_I = listAxisData[i][1][1] - listAxisData[i][0][1]
                yLength_J = listAxisData[j][1][1] - listAxisData[j][0][1]
                # print("xLTop -> {0} | yL_I -> {1} | yL_J -> {2}".format(xLengthTop,yLength_I,yLength_J))
                if(yLength_I == yLength_J):
                    if(xLengthTop * yLength_I >= min_area):
                        result += 1
        return result

print(count_rectangles([[0,0],[0,3],[5,3],[5,0],[9,9]], 15)) # 1
print(count_rectangles([[8,7],[8,2],[5,5],[3,7],[3,2],[1,1],[1,5],[5,1]], 15)) # 2
print(count_rectangles([[8,7],[8,2],[5,5],[3,7],[3,2],[1,1],[1,5],[5,1]], 20)) # 1