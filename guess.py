#! python3
''' This is a guess the number game.'''

import random

guessesTaken = 0

myName = input('Hello! What is your name?\n')

number = random.randint(1, 20)
print ('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
	guess = int(input('Take a guess.\n'))

	guessesTaken += 1

	if guess < number:
		print ('Your guess is too low.')

	if guess > number:
		print ('Your guess is too high.')

	if guess == number:
		print ('Good job, ' + myName + '! You guessed my number in ' + \
			str(guessesTaken) + ' guesses!')
		break

if guess != number:
	print ('Nope. The number I was thinking of was ' + str(number))

input ('<Press any key to exit...>')