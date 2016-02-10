import random

rand_num = random.randint(1, 10)

while True:
	guess = int(input("Guess the number: "))

	if guess == rand_num:
		print("Yep! The number was {}".format(rand_num))
		break
	else:
		print("Guess again!")

			