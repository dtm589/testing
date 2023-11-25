import random

number = random.randint(1, 10)

playerName = input("Hello what is your name? ")
numberGuesses = 0
print('I\'m glad to meet you, {}! \nLet\'s play a game today. I will think of a number between 1 and 10, then you will try to guess it. \nDon\'t forget, you only have 3 chances so guess:'.format(playerName))

while numberGuesses < 3:
    guess = int(input())
    numberGuesses += 1
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is to high.')
    if guess == number:
        break
    
if guess == number:
    print('Congratulations {}, you guessed the number in {} tries!'.format(playerName, numberGuesses))
else:
    print('Nice try, but you couldn\'t guess the number. \nWell, the number was {}'.format(number))