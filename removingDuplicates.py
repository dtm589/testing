'''
Complete the remove_duplicates function.

It should iterate over all the follower counts in the nums and remove all the duplicate numbers, then return the list of unique follower counts.

We want to preserve the order of the list so be careful when using a set!
'''

def remove_duplicates(nums):
    final_list = []
    for num in nums:
        if num not in final_list:
            final_list.append(num)
    return final_list