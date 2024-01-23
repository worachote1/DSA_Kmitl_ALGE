def find_most_frequent_substring (text, length):
    	#Write your code here
        result = ""
        vowel = ["a","e","i","o","u"]
        data = {}
        possibleResult = []
        for i in range(len(text)-length+1):
            temp_ss = ""
            for j in range(i,i+length):
                  temp_ss += text[j]
            for item in temp_ss:
                  if(item in vowel):
                        data[temp_ss] = data.get(temp_ss,0) + 1
                        break
        
        cntMax = float('-inf')
        for item in data:
            if(data[item] >= cntMax):
                  cntMax = data[item]
        for item in data:
            if(data[item] == cntMax):
                  possibleResult.append(item)
        
        possibleResult.sort()
        result = possibleResult[0]
        return result

# print(find_most_frequent_substring("kmnapkmnapsokmnkmnap",3))
# print(find_most_frequent_substring('aksskaaskakaskasakakss', 2))
print(find_most_frequent_substring('thisisalongsentencealongwithsomeaaaa', 4))