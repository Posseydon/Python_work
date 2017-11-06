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
if human != way:
	human = int(input("try your luck, choose a number from 1 to 9:"))

	if human <= 5:
		print("You will go to the left and you find wild beast, he attack you")
		fight = randint(1, 9)
		first_try = -1

		if first_try != fight:
			first_try = int(input("try your strength, choose a number from 1 to 9:"))
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

print("Welcome to the second part our game")
print("When you stay under the door to the castle, You see a large encoded door lock")
print("this door lock has a code of 10 numbers, you need to open these doors. To do this, you need to find a number that has 3 digits")

code = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in code:
	print(str(i) + "0")

your_code = int(input("you need to enter the code: "))
if your_code == 100:
	print("You guessed, you can go")
else:
	print("this is not the correct answer")
	exit()
	pass
print("You go inside the big room and see the owner of the castle")
print("He asked you:")

ask1 = input("You will want continue the game, y/n?")

if ask1 == "y":
	print("You are can continue game and go to the second room")
else:
	print("youy game is finished")
	pass
print("You inside second room")

player = input("You see one guy, he tell you: Do you want play with me? y/n: ")

if player == "y":
	print("Ok, let's go to play")
else:
	print("Ok, you can go out from the castle, but you don't have any award")
	pass

print("GAME")

human_player = randint(1, 14)

human_try = 4
while human_player != human_try:
	human_try_guess = int(input("you lucky number from 1 to 14: "))
	if human_try_guess != human_try:
		print("you wrong")
	else:
		print("You guessed, congratulation, you pick up a gold ducky, this is you award. Good by")
		exit()
		pass
	pass
