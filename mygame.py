from random import randint
print ("Hello, this is my first game")

player = str(raw_input ('your name: '))

print("Hello {}").format(player)
first_step = str(raw_input("Do yo want to start game? y/n:"))

if first_step == "y":
	print("You go to old forest, and you will have two ways: ")
else:
	print("You do not continue the game, ok see you later")
