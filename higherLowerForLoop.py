import random as rd
answer = rd.randint(1,20)
# display a welcome message
print("Hey, welcome to guess my number between 1 and 20")
# set up the game with 4 attempts possible.
for i in range(4): 
  # take user input and store as an integer in 'guess'
  guess = int(input("Number: "))
  
  if guess == answer:
    print("Well done!")
    # break the loop in case they guess successfully
    break
  elif guess < answer:
    print("Too low!")
  elif guess > answer:
    print("Too high!")
  
  if i == 3:
    print("Better luck next time, the answer was:",answer)

input("Thanks for playing! [ENTER] to end")
