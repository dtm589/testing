'''
Socialytics needs search capabilities! For now, we'll build something slow but simple. Our users want to give us the full name of a fellow Instagrammer, and we need to find them by checking if their first and last names exist in our database.

Complete the does_name_exist function. It should loop over all of the first/last name combinations in the first_names and last_names lists. If it finds a combination that matches the full_name it should return True. If the full name isn't found, it should return False instead.
'''

def does_name_exist(first_names, last_names, full_name):
    for fname in first_names:
        for lname in last_names:
            if fname + ' ' + lname == full_name:
                return True
    return False
