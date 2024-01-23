def count_pairs (number_list, distance):
    result = 0
    number_list.sort()
    for i in range(len(number_list)-1):
        for j in range(i+1,len(number_list)):
            if(number_list[j] % number_list[i] == 0):
                digitLeftA = number_list[i] % 10
                digitLeftB = number_list[j] % 10
                if(abs(digitLeftA-digitLeftB) <= distance):
                    result += 1
    return result

print(count_pairs([13,11,27,26,99,22],3))
