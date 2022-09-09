def moveElementToEnd(array, toMove):
    pL = 0
    pR = len(array)-1

    while(pL<pR):
        while(pL<pR and array[pR]==toMove):
            pR-=1
        if(array[pL]==toMove):
            #swap
            temp = array[pL]
            array[pL]=array[pR]
            array[pR]=temp

        pL+=1
    return array


arr1 = [2, 1, 2, 2, 2, 3, 4, 2];
print(moveElementToEnd(arr1,2))