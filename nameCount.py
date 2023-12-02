'''
Complete the count_names function.

It should iterate over all the names in the nested list_of_lists and count all the instances of target_name, then return the count.


'''

def count_names(list_of_lists, target_name):
    count = 0
    for list in list_of_lists:
        for name in list:
            if name == target_name:
                count += 1
    return count