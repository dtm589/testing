'''
Complete the sum function. Write it as a modified version of the sum algorithm that accepts a list of numbers and returns the sum of all of them.
'''

def sum(nums):
    total = 0
    for num in nums:
        total += num
    return total