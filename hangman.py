import random

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

def printGameDisplay( game ):
    # newList = game
    newList = []
    for i in range( len( game ) ):
        # append adds an item to the end of our list.
        newList.append( game[i] + ' ')
    # this is a bit of a workaround to get all the items in the list to join together
    # into a single string for printing.
    print(''.join(newList))

def checkGameStatus( game ):
    if '_' in game:
        return True
    else:
        print("Congratumalationers! You have won many przs!")
        return False

# Here's our bucket of potential words. You can include any words you like.
wordsToGuess = ['apple', 'banana', 'cranberry', 'dragonfruit', 'elderberry', 'fig', 'grapefruit', 'honeydew']

# I did have the next three lines as a single line but splitting it up should help
# you understand what's going on more easily.
# Create a random number between 0 and the final position of the wordsToGuess list.
answerPosition = random.randint(0, len(wordsToGuess) - 1)
# Store the actual word in a string by retrieving it from the list
answerString = wordsToGuess[ answerPosition ]
# Convert the string to a list using the list function to allow us to change it
answerList = list( answerString )
# Store the length of the answer in a variable for use later in the program (saves typing)
answerLength = len( answerList )

# Create a list of underscores the same length as the answer
gameDisplay = list( '_'*len(answerList) )

# Welcome message and useful testing information
print("Welcome to the fruit guessing game!")
# print( "For testing purposes the answer is:", ''.join(answerList))

# Define all necessary variables
gameStatus = True
badGuesses = 0

# The game loop
while gameStatus == True:
    userGuess = input("Guess a single letter: ")
    if userGuess in answerList:
        print( "Correct guess!")
        for i in range( answerLength ):
            if userGuess == answerList[i]:
                gameDisplay[i] = userGuess
        printGameDisplay(gameDisplay)
        gameStatus = checkGameStatus( gameDisplay )
    else:
        print( HANGMAN_PICS[ badGuesses ] )
        # badGuesses.append( userGuess )
        badGuesses = badGuesses + 1
        # check they have remaining guesses
        if badGuesses == len(HANGMAN_PICS):
            print("You lose!! The answer was: ", answerString)
            gameStatus = False




