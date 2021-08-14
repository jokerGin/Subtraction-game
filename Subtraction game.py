#simple game
message = 'Hello guys I\'m back today with a game.'
message += '\nHope you enjoy it and kindly follow the rules. '

print(message) #Greets players

from random import randint

num = randint (20,30)
#creates the number we start from
print (f'The starting number is {num} .')

while True:#creates the loop
	
	rules = '\nEnter a number between 1 and 3. \n'

	userNum = int(input(rules))
#Takes the input from the user
	if userNum > 3:
		print('You broke the rules !!!')
		break

	else:
		compNum = randint(1,3)
		num -= userNum

		if num <= 0:
			print(f'{num}, \nYou lose !!!')
			break
	if num > 0:
		num -= compNum

		if num <= 0:
			print("You win !!!!")
			break






		




