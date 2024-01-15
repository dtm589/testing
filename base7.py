'''
Given an integer num, return a string of its base 7 representation.
'''

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        result = ""
        sign = "" if num >= 0 else "-"
        num = abs(num)

        while num > 0:
            remainder = num % 7
            num //= 7
            result = str(remainder) + result

        return sign + result