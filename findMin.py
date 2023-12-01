'''
In each assignment in this course we'll be building out pieces of a pretend product: Socialytics - The tool you need to track your growth as an Instagram influencer. We need to display to our influencers the people they follow who have the lowest follower count. This will help them know which of the people they follow aren't popular enough to be worth following anymore.

Implement the "find min" algorithm in Python by completing the find_min() function.
'''

def find_min(nums):
    min = float("inf")
    for num in nums:
        if num < min:
            min = num
    return min