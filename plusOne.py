'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for num in digits:
            string += str(num)
        
        temp = str(int(string) +1)

        return [int(temp[i]) for i in range(len(temp))]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n-1, -1, -1):
            if(digits[i] == 9):
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        
        digits.insert(0,1)
        return digits
