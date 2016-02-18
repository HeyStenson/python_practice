import random

words = ['red', 'green', 'yellow', 'kittens', 'puppies', 'parakeets']

while True:
 	start = input("Press Enter to start or Q to quit. ")
 	if start.lower() == 'q':
 		break

 	secret_word = random.choice(words)
 	wrong_guesses = []
 	correct_guesses = []

 	while len(wrong_guesses) < 7 and len(correct_guesses) != len(list(secret_word)):
 		for letter in secret_word:
 			if letter in correct_guesses:
 				print(letter, '\n')
 			else:
 				print('_', '\n')

 		print('')
 		print('Strikes: {}/7'.format(len(wrong_guesses)))		
 		print('')

 		guess = input('Guess a letter: ').lower()

 		if len(guess) != 1:
 			print("You can only guess one letter")
 			continue
 		elif guess in wrong_guesses or guess in correct_guesses:
 			print("You've already tried that one")
 			continue
 		elif not guess.isalpha():
 			print("You can only guess letters")
 			continue

 		if guess in secret_word:
 			correct_guesses.append(guess)
 			if len(correct_guesses) == len(list(secret_word)):
 				print("You win! The word was {}".format(secret_word))
 				break
 		else:
 			wrong_guesses.append(guess)
 	else:
 		print("You didn't guess it! The word was {}".format(secret_word))					
 			
