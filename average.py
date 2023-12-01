'''
Complete the average_followers function. It should return the average of the given list of numbers.
'''

def average_followers(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)