'''
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.
'''

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisor_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisor_sum += i

        return divisor_sum == num