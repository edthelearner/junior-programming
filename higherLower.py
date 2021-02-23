import random as rd
answer = rd.randint(1,20)
print("Hey, welcome to guess my number between 1 and 20")
guesses = 0
while guesses < 4 : 
  guess = int(input("Number: "))
  if guess == answer:
    print("Well done!")
    break
  elif guesses == 3:
    print("Better luck next time!")
    print("The answer was",answer)
    guesses += 1
  else:
    print("Try again, yo!")
    guesses += 1

input("Thanks for playing! [ENTER] to end")
