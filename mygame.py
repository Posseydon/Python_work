from random import randint
print ("Hello, this is my first game")

player = input ('your name: ')
print("Hello" + " " + player)
print("Let's try will play")

first_step = str(input("Do yo want to start game? y/n:"))

if first_step == "y":
	print("You go to old forest, and you will have two ways: ")
else:
	print("You do not continue the game, ok see you later")
	exit()


way = randint(1, 9)
human = -1

print("You must change your fate")
while human != way:
	human = int(input("try:"))

	if human <= 5:
		print("You will go to the left and you find wild beast, he attack you")
		fight = randint(1, 9)
		first_try = -1	
		
		while first_try != fight:
			first_try = int(input("Your shock:"))
			if first_try >= 5:
				print("You win go to the castle")
			else: 
				print("You lose, sorry...")
				exit()
				pass
		pass
	else: 
		print("Welcome to the castle")
	pass
pass



