'''
We need to be able to search our Socialytics user base more quickly! Our users are complaining that the search bar is painfully slow. You'll notice that if you run the code in its current state, it will take a very long time.

The find_last_name function takes "names_dict", a dictionary of first_name -> last_name. It also accepts a first_name. If first_name is a key in the dictionary, find_last_name returns the associated last name. If the key is not found, it returns None. Make sure you handle the case where the first_name is not in the dictionary!

Write the function so that it runs quickly! It should be O(1).
'''

def find_last_name(names_dict, first_name):
    if first_name in names_dict:
        return names_dict[first_name] 
    return None