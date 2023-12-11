'''
Complete the get_num_guesses function. It takes a password length as input and returns the number of guesses required to ensure that a password of that length or shorter is guessed.
'''
def get_num_guesses(length):
    total = 0
    for i in range(length):
        total += 26 ** (i +1)

    return total