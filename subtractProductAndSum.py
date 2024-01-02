'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sums = 0
        for num in str(n):
            digit = int(num)
            product *= digit
        
        for num in str(n):
            digit = int(num)
            sums += digit
        
        return product - sums