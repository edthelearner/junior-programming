# import any additional libraries
import random
import time

# define functions
def printIntro():
  print("Welcome to Dragon Realm 5")
  time.sleep(2)
  print("You are walking along a track on a distant planet")
  time.sleep(2)
  print("A fork in the track appears ... to the left, down into a gorge")
  time.sleep(2)
  print("To the right, along the ridgeline back to base")
  time.sleep(2)

def getPlayerChoice():
  choice = input("Which direction do you choose? [L] or [R], or toss a coin[C]: ")
  if choice == 'L':
    print("You selected left")
    goLeft()
  elif choice == 'R':
    print("You said right")
    goRight()
  elif choice == 'C':
    print("You want to toss a coin. Brave!")
    flipCoin()
  else:
    print("You didn't enter a valid choice, ya dumby. You starve.")

def goLeft():
  #program what you want to happen if the user goes left.
  print("You're in the gorge")
  time.sleep(2)
  print("You stumble across the Dragon Realm 5")
  time.sleep(2)
  print("In your excitement, you die of a heart attack.")
  time.sleep(2)

def goRight():
  #program what you want to happen if the user goes right.
  print("You walk along the ridgeline")
  time.sleep(2)
  print("You trip and land on a sharp rock.")
  time.sleep(2)
  print("This leads to you discovering the meaning of life. Well done.")
  time.sleep(2)

def flipCoin():
  theCoin = random.randint(1,2)
  if theCoin == 1: 
    goLeft()
  elif theCoin == 2:
    goRight()
  else:
    print("The coin is not 1 or 2, Mr Wilson you have made a mistake.")

# The game loop begins
gameContinue = True
while gameContinue == True:
  printIntro()
  getPlayerChoice()
  
  playAgain = input("[Y] to play again, anything else to exit.")
  if playAgain != 'Y':
    gameContinue = False

# graceful exit
input("[ENTER] to end.")

  
