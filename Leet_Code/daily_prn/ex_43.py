class Solution:
    def multiply(self, num1: str, num2: str):
        data = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, "7": 7, "8": 8, "9": 9}
        num_one = num_two = 0
        for i in range(len(num1)):
            num_one += pow(10,len(num1)-1-i) * data[num1[i]]
        for i in range(len(num2)):
            num_two += pow(10,len(num2)-1-i) * data[num2[i]]
        return str(num_one*num_two)
