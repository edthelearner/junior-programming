# Import any necessary libraries
import random
import time

green = '\033[32m'
yellow = '\033[33m'
red = '\033[31m'
blue = '\033[34m'
white = '\033[37m'
magenta = '\033[35m'

# Xavier this might not work with your colours but see how you go.
def printAndSleep(theText, theTime):
    print(theText)
    time.sleep(theTime)

def TheName():
    print(magenta + "Welcome player you are now playing Serbian Call of Duty" + white)
    time.sleep(3)

def PrintIntro():
    print('')
    print("Hello Comrad and Welcome to the land of Sokovia in Serbia,")
    time.sleep(3)
    print("i am General Spiridon Visko,")
    time.sleep(3)
    print("and i will be guiding you through your top secret mission to collect the president of Serbia who was captured by the dreaded Americans")
    time.sleep(3)
    # name will only be available inside this function. If you try to call name outside here it will crash.
    name = input("So Comrad what is your name? ")
    time.sleep(3)
    print(name + ", of course now lets give you the assignment and start this really urgent mission")
    time.sleep(3)
    print("Ok " + name + " your first assingment is to retrieve the password to a top secret safe that the Amercians have have hid away in one of their bases near Nevada")

def FirstMission():
    print('')
    time.sleep(3)
    print("okay you've got that now lets gear up and head off Comrad no time to waste.")
    time.sleep(3)
    print('''Now comrad there are a few weapons to choose from so pick whatever one you like...''')
    
    # 'b' is not a descriptive variable choice. What about weapon? Wouldn't that be better?
    b = input(yellow + '''[a] mp40
                        [b] ak-47 
                        [c] a4-a1 
                        ''' + white)
    if b == "a":
        time.sleep(3)
        print(blue + "alright comrad you have decided to use the trusty mp40 this thing will blow your mind enjoy the carnage! " + white)
    elif b == "b":
        time.sleep(3)
        print(green + "ahh the classic ak-47 good choice, now we can create some havoc comrad!" + white)
        time.sleep(3)
    elif b == "c":
        time.sleep(3)
        print(red + "ok comrad the a4-a1 the American teenages love these things." + white)
    else:
        time.sleep(3)
        print("Looks like you are going in without a weapon, comrad you seem very confident.")
    time.sleep(3)
    print("alright now that you have chosen a weapon we can head off to get our president back!")
    time.sleep(3)
    # You call the CarryON function here, but then also call it in the main program.
    CarryON()

def CarryON():
    print('')
    time.sleep(1)
    print('''now this mission is very important and we need to infiltrate the base to find this safe with the top secret passcode,
    and we need to do this correctly so this decision is all yours comrad would you like to.''')
    
    c = input(yellow +'''[a] go in guns blazing 
    [b] stealthy taking out every gaurd in silence 
    ''' + white)
    if c == "a":
        time.sleep(3)
        print(blue + '''alright comrad you want to run guns blazing i like your style however we need to find the code to the secret safe that they have hid in this base,
        and only the highest ranked officer has it so they will try and run if they hear us so we need to be quick. '''+ white)
        loud()
    elif c == "b":
        time.sleep(3)
        print(green + '''now this is a good choice comrad but be quick the highest ranked officer is having a meeting in the confrence room,
        and he has the code to the safe which is prioty number 1 now lets put our silencers on and start heading off.'''+ white)
        silence()

def loud():
    answer = random.randint(1,3)
    
    time.sleep(3)
    print("lets go comrad! the officer is in the conference room at the moment so we will covr you so you can run up there and catch the scum ")
    time.sleep(2)
    d = int(input(magenta + '''you have found the officer and he starts running as quick as possible,
    you have eliminated the others in the meeting but you lose him after turning the corner,
    there are three different cupboards and no where else he could of gone so you now have a choice,
    choose the correct cupboard otherise it may end badly. 
    ''' + white))
    # What choices does the player have? Do they know they're guessing a number between 1 and 3?
    if d == answer:
        time.sleep(2)
        print(blue + "well done he was inside the ", answer ," box, good choice now grab the passcode from him and make your way back to General Spiridon."+ white)
        print(yellow + "*remember the code the officer gave was #34987* lets hope he was telling the truth"+ white)
        passcode()
    elif d != answer:
        time.sleep(2)
        print(green +'''oh no you have chosen the incorrect box, 
        the officer then exits from cupboard number ''' , answer ,''' and shoots you in the chest killing you and your dreams of completing this mission better luck next time, 
        '''  + white)
        ending()

def silence():
    print('')
    time.sleep(2)
    print("comrad you will be running up to the conference room quietly there might be a few gaurds there so make sure to take them out silently we can not afford for the officer to leave this base.")
    time.sleep(2)
    print(magenta +'''you have made it to the conference room however there are two gaurds standing and protecting the door,
    the one gaurd leaves the door to assisst a lady but he is standing by the balcony which could risk your team being found so you have two choises will you,''' + white)
    silent = input(yellow +'''[a] kill the gaurd and the lady to help save your team.
    [b] kill the stranded gaurd at the door and grab the officer from the conference room the choice is yours. 
    '''+ white)
    if silent == "a":
        time.sleep(2)
        print(blue + '''you have eliminated the gaurd and the lady however the gaurd by the door has noticed the gunfire,
        the gaurd then warns the base and they lock the palce down, 
        the Americans then kill everyone in your team one by one.''')
        ending()
    elif silent == "b":
        time.sleep
        print(green + '''you have killed the gaurd and entered the room,
        the officer is with two others,
        you then eliminate them leaving the officer on his own, he gives up and hands the passcode over,
        and lucky for you Spiridon noticed the gaurd by the balcony and took him out before he notcied the team.'''+ white)
        time.sleep(3)
        print(yellow + "*remember the code the officer gave you was #19009*" + white)
        passcode()

def ending():
    print('')
    time.sleep(2)
    print('''better luck next time, will you like to''')
    again = input(yellow +'''[a]restart 
    [b]sign out 
    '''+ white)
    if again == "b":
        time.sleep(2)
        print(green + "okay we hope to see you again." + white)
        dark()
    elif again == "a":
        time.sleep(2)
        print(blue + "alright i hope this time goes better, enjoy." + white)
        time.sleep(1)
        print('''where exactly do you want to start''')
    
    where = input(yellow +'''[a]beginning
    [b]at the first mission
    ''' + white)
    if where == "a":
        PrintIntro()
    elif where == "b":
        FirstMission()
        

def passcode():
    print('')
    time.sleep(2)
    print('''Well done Comrad you found the passcode now we can make our way to the safe and enter the code in,
    if we get the code wrong the safe will self-estruct so lets hope that officer gave us the correct code. ''')
    
    time.sleep(2)
    passcodes = input('''the officer gave you the code now repeat it into the safe 
    ''')
    # This is hidden! Tough game
    if passcodes == "#19009*":
        time.sleep(2)
        print(blue + "that is the correct code, the safe opens and inside is a key, the key that will open the hatch that they have hid our prsident in."+ white)
        SecondMission()
    elif passcodes == "#34987*":
        time.sleep(2)
        print(green + "Oh no that was the incorrect code, the safe then self-destructs and kills you and your team ending the mission entirely, better luck next time. " + white)
        ending()
    else:
        time.sleep(2)
        print(red + "Oh no you entered the incorrect passcode, the safe self-destructs killing you and everybody in the base." + white)
        ending()
def SecondMission():
    print('')
    time.sleep(2)
    print('''Well done Comrad i am very proud of you, but now that we have this key we can finally find and capture the President from the base,
    lucky for us we alreay know where the base and the hatch is so all you need to do is take the key to the hatch,
    eliminate any enemies that come your way and finally grab the President and swiftly leave the building if there are any puzzles in the way you can solve them,
    good luck soldier i'll see you on the otherside''')
    
    # This is a long time to wait
    time.sleep(6)
    print(magenta + '''You and your team arrive to the base and have eliminated all gaurds outside, you have the option to either,''' + white)
    
    door = input(yellow + '''[a] go through the main hallway with the rest of your team or
    [b[ go solo through a side door. 
    '''+ white)
    if door == "a":
        time.sleep(3)
        print(blue + '''You have chosen to stick with your team,
        your team then enters the building but are gettig shot from every angle 
        everyone is falling and diving all around you 
        you try your hardest but get shot in the shoulder by a man on your left
        you struggle to find help and after realising that the rest have done the same you start to see black,
        a weird figure approaches and shoots you in the head'''+ white)
        ending()
    elif door == "b":
        time.sleep(3)
        print(green + '''You have chosen to go solo,
        you enter through the door and you see nothing but paper and books
        you hear faint gunshots from the other room
        you panic and look around the room and find a door 
        you slightly open the door and see a hatch with a lock unprotected
        could this be the hatch with the president.'''+ white)
    time.sleep(5)
    print('''Will you''')
    
    hatch = input(yellow +'''[a]unlock the hatch
    [b]leave and help your team
    ''' + white)
    if hatch == "a":
        time.sleep(2)
        print(blue + '''You have chose to open the hatch,
        the hatch opens but there is another door but this time there is a keypad with letter,
        on the keypad it says guess letters and if correct you will be able to enter'''+ white)
        time.sleep(2)
        GuessTheWord( 'game' )
    elif hatch == "b":
        print(green + '''You have chosen to turn around and help your team,
        you enter the room and your entire team are on the ground dead the Americans ntice you and they take turns shooting at your now dead body'''+ white)
        ending() 

def GuessTheWord( game ):
    # Xavier I'm not sure what you're trying to do here.
    # There are no code comments in this document either, making it harder.
    # Why does this function have a parameter called 'game'?
    print('')
    newList = []
    for i in range( len( game ) ):        
        newList.append( game[i] + ' ')
    print(''.join(newList))
    # Aren't these the words to guess? Not 'game'?
    wordsToGuess = ['raccoon', 'lion', 'fox', 'turtle', 'kangaroo', 'platypus', 'octopus', 'hammerhead shark']

    answerPosition = random.randint(0, len(wordsToGuess) - 1)
    answerString = wordsToGuess[ answerPosition ]
    answerList = list( answerString )
    answerLength = len( answerList )
    gameDisplay = list( '_'*len(answerList) )

    time.sleep(2)
    print("It says to guess any letter ")
    print("this is to test the answer is:", ''.join(answerList))
    gameStatus = True

    while gameStatus == True:
        guess = input('''Now enter a letter and find out if you are correct
        ''')
        if guess in answerList:
            print("Yes, that letter is in the word")
            for i in range( answerLength ):
                if guess == answerList[i]:
                    gameDisplay[i] = guess
            GuessTheWord(gameDisplay)
        elif guess == "guess":
            print('Well done you have opened the door')
            door()
        else:
            print("oh no that is an incorrect guess and the gaurds inside the door have been alerted and ope the door themselves and eliminate you.")
            ending()
            gameStatus = False

def door():
    print('')
    time.sleep(2)
    print(magenta + '''You open the door, the gaurds notice you but you take them out 
    you find the President on the floor
    you grab him and you start running for the exit 
    you look around and see everyone on the floor dead however the helicopter is still nearby
    you straight to the helicopter with the President in the seat beside you ''' + white)
    time.sleep(5)
    cc = input('''Thank you so much brave soldier what could i do to repay you? 
    ''')
    print(blue + " you want me to " + cc + " dont worry i'll try my best, Thank you again soldier."+ white)
    finished()

def finished():
    print('')
    print(magenta + '''Well done player you have completed the game choosing all of the correct choses well done, will you like to restart''' + white)
    
    agains = input(yellow +'''[yes]
    [no]
    '''+ white)
    if agains == "yes":
        print(blue + "alright enjoy"+ white)
        PrintIntro()
    elif agains == "no":
        print(green + "Alright we hope to see you again" + white)


def dark():
    print("")

# Main program
TheName()
PrintIntro()        
FirstMission()
CarryON()    




        