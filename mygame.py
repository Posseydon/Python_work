import random

print ("Hello, this is my first game")
#What is your name?
player = input ('your name: ')
#we glade to see you
print("Hello" + " " + player)
print("Let's try will play")
#Our game is strting
def start(first_step):
	if first_step == "y":
		return("You go to old forest, and you will have two ways: ")
	quit()
start(str(input("Do yo want to start game? y/n:")))

#The next step, we g
print("You must change your fate")

def battle(human):

	if human <= 5:
		print("You will go to the left and you find wild beast, he attack you")
		def beast(first_try):
			if first_try >= 5:
				return("You win go to the castle")
			print("You have lost, sorry ... you go on, but you only have half lives")
		beast(int(input("try your strength, choose a number from 1 to 9:")))
	print("Welcome to the castle")

battle(int(input("try your luck, choose a number from 1 to 9:")))

print("Welcome to the second part our game")
print("When you stay under the door to the castle, You see a large encoded door lock")
print("this door lock has a code of 10 numbers, you need to open these doors. To do this, you need to find a number that has 3 digits")


def out_door(your_code):

	while your_code != 5:
		return("this is not the correct answer, one more please")
	print("You guessed, you can go")

out_door(int(input("you need to enter the code from 1 to 9: ")))

print("You go inside the big room and see the owner of the castle")
print("He asked you:")

def question(ask1):
	if ask1 == "y":
		return("You are can continue game and go to the second room")
	quit()

question(str(input("You will want continue the game, y/n?")))

print("You inside second room")

def easy_play(player):
	if player == "y":
		return("Ok, let's go to play")
	print("Ok, you can go out from the castle, but you don't have any award")

easy_play(input("You see one guy, he tell you: Do you want play with me, you need to guess the number?y/n: "))

print("GAME")

def rand_number(human_player):
	lucky = random.randrange(1, 10)
	print(lucky)
	if human_player == lucky:
		return("You guessed, nice game")
		quit()
	print("you mistaken try again")
	return(rand_number(int(input("What Your lucky number?: "))))

print(rand_number(int(input("What Your lucky number?: "))))
