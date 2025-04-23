#python 3.7.9

#This program is a baisc text based adventure that plays in the python shell

#Created by George Peter Thom

#Game Book content was written when I was a child, so themes and grammar
#may be slightly off, but I wanted to use the imagination of my younger self
#in this program to bring an old childhood dream to life using python code.
#red numbers refer to game book document file paragraph numbers

#the original book was written in a word document, i've tried to impliment it in code

#at this time there is no way to win! sorry! you win by playing!

#also at this time some of the options may lead to dead ends as they have not been written into the code yet

#hangman has a bug where if you don't guess the letter in 10 turns it just bugs out, i basically made it too messy and couldn't fix it in time
import time
import random




#Title Screen
def levelone():
    time.sleep(1)
    
    print("""
 _______  _______  _______  _______  _______ 
|       ||       ||   _   ||       ||       |
|  _____||    _  ||  |_|  ||       ||    ___|
| |_____ |   |_| ||       ||       ||   |___ 
|_____  ||    ___||       ||      _||    ___|
 _____| ||   |    |   _   ||     |_ |   |___ 
|_______||___|    |__| |__||_______||_______|
""")


    print("You are the captain of the explorer ship “voyager”")
    time.sleep(1)
    print("your mission is to find new worlds and new civilizations,")
    time.sleep(1)
    print("to boldly go where no Bidro (alien) has been before!")
    
    print("""
  ___________________          _-_             
  \__(==========/_=_/ ____.---'---`---.____    
              \_ \    \----._________.----/    
                \ \   /  /    `-_-'             
            __,--`.`-'..'-_                 
           /____          ||                    
                `--.____,-'
                """)

    print("")
    print("“Sir we have just spotted a black hole, it came out of no where and now it is pulling us in!”")
    time.sleep(1)
    print("a Bidro called Frum shouts, you give the order to put all power to the reverse engines,")
    time.sleep(1)
    print("but this does not work as the black hole's gravity is too strong and your ship begins to be pulled in!")
    time.sleep(1)
    print("every body straps themselves down and braces for impact.")
    time.sleep(1)
    print("you all black out as you enter the gaping maw.")
    time.sleep(1)
    input("~~~Hit Enter~~~")#141
    level3()
#asteroid orbit level was never implemented, but kept in for historical code sake   
def level2():
    print("")
    print("The ship moves towards the large asteroid and makes an orbit.")
    print("you can see some large craters on it,")
    print("your motion tracker is detecting lots of asteroids in motion...")
    choice = input("Do you beam down (1) or move on some were else (2)")#60,19
    if choice == "1":
        level60()
    elif choice == "2":
        level19()
#First Level and chocies, so far sheilds lead to death and random selcetion of colours that changes each time you play
#evasive action follows on to a more story driver route
#deploying guns leads to random encounter
#hangman leads to death
def level3():
    print("")
    print("When you wake up you check all the ships report screens...")
    time.sleep(1)
    print("you see that nobody is hurt but it isn’t over yet,")
    time.sleep(1)
    print("you have come out of the void into an asteroid field")
    time.sleep(1)
    print("you must have passed through a worm hole.")
    time.sleep(1)
    print("A couple small meteors bounce off your ships hull,")
    time.sleep(1)
    print("what is your first order;")#141
    time.sleep(1)
    choice = input("Do you turn on your shields (1) take evasive action (2) or deploy your guns (3) or play hangman on the ships computer (4)")
    if choice == "1":
        level30()          
    elif choice == "2":
        level20()
    elif choice == "3":
        choosePath()
    elif choice == "4":
        hangman()
    else:
        deadfunc3()
#you avoid the danger for now in this level, but you only have options that lead to the dead function()       
def level20():
    print("")
    print("The ship swerves to avoid the incoming asteroids")
    time.sleep(1)
    print("“evaisive pattern delta!”")
    time.sleep(1)
    print("a medium sized asteroid hits one of you engines!")
    time.sleep(1)
    print("followed by another that hits the bottom of the ship!")
    time.sleep(1)
    print("then your ship’s designated Spock shouts")
    time.sleep(1)
    print("“I suggest we turn on our shields captain”")
    time.sleep(1)
    choice = input ("do you do what he suggested (1) deploy your guns and shoot the asteroids (2) or continue taking evasive action (3)")#30, 40, 50
    if choice == "1":
        level30()
    elif choice == "2":
        choosePath()
    else:
        deadfunc2()
    
def level30():
    print ("")
    time.sleep(1)
    print("Your shields power up and flash 5 RANDOM Colours")
    colours=["Bule","Red","Orange","Lime Green","Brown","Yellow","Purple"]
    print(random.sample(colours, k=5))
    input("Hit Enter")
    deadfunc2()

##this choice was never implemented, but kept it in for historical code sake
def level39():
    print("")
    print("Hugo puts on his space suit and gets into the transporter room with you,")
    print("the Bidro on the controls press’s some buttons and you both beam down.")
    print("You both appear on the asteroid.")
    print("It is very baron.")
    print("“Nothing coming up on scanners, apart from some faint seismic activity from the core of the asteroid” Hugo states")
    print("There is an ominous looking crack to the left,")
    choice = input("do you investigate it (49) or beam up to the ship and continue looking for new environments (29)")#49, 29
    if choice == "1":
        level49()
    elif choice == "2":
        level29()

#deploying guns leads here, random encounter with asteroids, you have to choose which one to shoot and it could be right or wrong
#this loops back on itself untill you get destroyed
def choosePath():
    correctPath = random.randint(1, 2)
    print("")
    time.sleep(1)
    print("You enter a RANDOM encounter...")
    print("You begin to shoot the asteroids with lazer beams")
    time.sleep(2)
    print("there's TWO asteroid's nearby that are coming towards the ship")
    time.sleep(2)
    print("Shoot it down!")
    path = ""
    while path != "1" and path != "2": #input validation
        chosenPath = input("which asteroid will you shoot? (1 or 2): ")
        if chosenPath == str(correctPath):
            print("Nice one, you got it")
            print("You are alive!")
            time.sleep(1)
            choosePath()
            break
        else:
            print("...")
            print("BANG")
            deadfunc2()
            break

    

    
    

#def level5():

def hangman():
    secretword = ["a"]
    displayedword = secretword[:]
    lives=10
    playagain = 0
    image1=['|   +===+']
    image2=['|   |    ']
    image3=['|   0    ']        
    image4=['|  /|\   ']
    image5=['|   |    ']
    image6=['|  / \   ']
    image7=['|        ']


    while playagain == 0 or playagain >0:
        if lives == 0:
            print ("GAME OVER")
            deadfunc2()
            break
        elif playagain <= 0:
            for i in range(len(displayedword)):
                displayedword[i]="*"
            print("""
            image1=['|   +===+']
            image2=['|   |    ']
            image3=['|   0    ']        
            image4=['|  /|\   ']
            image5=['|   |    ']
            image6=['|  / \   ']
            image7=['|        ']
            """)

            print('displayedword:', displayedword)
            print("The lives that you have curently: ",lives)


            guess=input("guess a letter ")

            livescount=0
            win="false"

            while lives >=0:
                for i in range(len(displayedword)):

                    if secretword[i]==guess:
                        displayedword[i]=guess
                        livescount=1

                    if (displayedword==secretword):
                        print("You Win!")
                        input("~ Hit Enter ~")
                        deadfunc4()
                        break
                    break
                    deadfunc()
                        
                        
                if livescount==0:
                    lives=lives-1
                    livescount=0
                
                else:
                    livescount=0

                print('displayedword:', displayedword)
                print("lives left: ", lives)
                print(image1)
                print(image2)
                print(image3)
                print(image4)
                print(image5)
                print(image6)
                print(image7)
                guess=input("guess a letter: ")
#different dead functions depending on how you died in the game.
def deadfunc():
    
    print("""
You are dead!
           ______
        .-"      "-.
      (              )
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
         

  """)
def deadfunc2():
    
    print("""
You are dead!
Game Over!
           ______
        .-"      "-.
      (              )
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
         

  """)
    input("Exit")    
    
def deadfunc3():
    
    print("""
You are dead because you didn't choose any option available!
Game Over!
           ______
        .-"      "-.
      (              )
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
         

  """)
    input("Exit")
def deadfunc4():
    
    print("""
You are dead because you played hangman instead of commanding your star ship!
Game Over!
           ______
        .-"      "-.
      (              )
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
         

  """)
    input("Exit")
#play again function always runs
Playagain = input (str("Would you like to play from the beginigng? type y or yes to start "))
while Playagain == "y" or Playagain == "yes":
    if Playagain == "y" or Playagain == "yes":
        levelone()
    else:
        break
    
print("nope")
deadfunc2()


        
