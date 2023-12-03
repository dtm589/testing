'''
At Socialytics we need to be able to compute the power set of a set of influencers. Something about targeting segments of an audience with ads. I don't know, I just do what I'm told.

A power set is the set of all possible subsets of a set. For example, the set {1, 2, 3} has the power set:

{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

We'll work with lists instead of sets for simplicity.
'''

def power_set(input_set):
    final_subset_list = []
    if input_set == []:
        return [[]]
    returned_list = power_set(input_set[1:])
    for list in returned_list:
        final_subset_list.append([input_set[0]] + list)
        final_subset_list.append(list)
    return final_subset_list