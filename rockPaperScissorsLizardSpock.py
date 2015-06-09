__author__ = 'Scott Gramig'
__program__ = 'Paper-Rock-Scissors-Lizard-Spock'

import random
import os

#global variables to track w/l/t
win = 0
loss = 0
tie = 0


def greeting():  # greets player and tells rule

	print("Let's play Rock-Paper-Scissors-Lizards-Spock!!")
	print("Rules:")
	print("0: Rock-------->beats Scissors and Lizard")
	print("1: Spock------->beats Rock and Scissors")
	print("2: Paper------->beats Rock and Spock")
	print("3: Lizard------>beats Paper and Spock")
	print("4: Scissors---->beat Paper and Lizard")
	print("\nLet's RO SHAM BEAUX!!!\n")


def gameLogic(playerChoice, compChoice):  # determines winner of round

	#dict for weapons for future use
	#weapons = {0: "Rock", 1: "Spock", 2: "Paper", 3: "Lizard", 4: "Scissors"}

	#access the global variables
	global tie, win, loss

	#game logic
	if playerChoice == compChoice:
		print("TIE!")
		tie += 1

	elif (playerChoice == 0 and compChoice == 3) or (playerChoice == 0 and compChoice == 4) or \
		   (playerChoice == 1 and compChoice == 0) or (playerChoice == 1 and compChoice == 4) or \
		   (playerChoice == 2 and compChoice == 0) or (playerChoice == 2 and compChoice == 1) or \
		   (playerChoice == 3 and compChoice == 2) or (playerChoice == 3 and compChoice == 1) or \
		   (playerChoice == 4 and compChoice == 2) or (playerChoice == 4 and compChoice == 3):
		print("YOU WIN!")
		win += 1
	else:
		print("YOU LOSE!")
		loss += 1

	print "Win: %d ----- Loss: %d ----- Tie: %d" % (win, loss, tie)


def gamePlay():  # all in a nice function :)))))
	greeting()
	userInput = raw_input("Make a choice 0-4 (input 9 to exit):")
	userInput = int(userInput)

	os.system('clear')

	#exit program
	if userInput == 9:
		exit()

	compChoice = random.randrange(0, 5)
	compChoice = int(compChoice)
	print("Computer choose %d" % compChoice)

	gameLogic(userInput, compChoice)

# main block

while 1:
	gamePlay()
