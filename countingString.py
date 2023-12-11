'''
Implement the count_potions function. It should take a list of our players' inventory (strings) as input and return the number of times Healing potion shows up in the list as an integer.
'''


def count_potions(inventory):
    count = 0
    for item in inventory:
        if item == 'Healing potion':
            count += 1
    return count