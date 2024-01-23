def check_perfect_list (numbers, distance):
    #Write your code here
    result = 1
    for i in range(len(numbers)-1):
        if(i == len(numbers)-2):
            if(not(abs(numbers[i] - numbers[i+1]) <= distance)):
                result = 0
                break
        else:
            if(not(abs(numbers[i] - numbers[i+1]) <= distance and abs(numbers[i] - numbers[i+2]) <= distance)):
                result = 0
                break
    return result

print(check_perfect_list([1,4,3,2,3],3))
print(check_perfect_list([10,2,11],5))