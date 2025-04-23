# import required module 
import random
from tkinter import*
import tkinter.font as tkFont
from tkinter import scrolledtext
from random import randint
import time
import linecache
#import pyautogui
import textwrap
import sys

#python 3.7.9

#This program creates a transparent Tkinter window in which random setences are remixed from Anti-Oedipus: Capitalism and Schizophrenia 1972 by Gilles Deleuze Félix Guattari 
#This program requires the text file anti_oedipus_chopped.txt

#tk window
window = Tk()
window.title('Data Stream')
window.geometry("1000x900")

#variables
stop = 1
loop = 1
aa = "help"
randnum = int(random.random()*355)
linenumberyin = randnum
linenumberyang = randnum

#font
helv36 = tkFont.Font(family="Helvetica",size=25,weight="bold")

#font color
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

#textbox
my_text= scrolledtext.ScrolledText(window, width=40, height=16, font=(helv36),fg='black')

#pack to window
my_text.pack(pady=20)

#start variables
startpos1=1
startpos2=50

endpos1=51
endpos2=100

#start and logic
def start():
    global stop
    stop = 1
    click()

# print random word
def sentencemaker():
    
    global aa
    # open file
    with open("anti_oedipus_chopped.txt", "r") as file:
        data = file.read()
        words = data.split()
      
    # Generating a random number for word position
        word_pos = random.randint(0, len(words)-1)
    
        a= (words[word_pos]+(" ")+words[word_pos+1]+(" ")+words[word_pos+2])   

    with open("anti_oedipus_chopped.txt", "r") as file:
        data = file.read()
        words = data.split()
      
    # Generating a random number for word position
        word_pos = random.randint(0, len(words)-1)
    
        b= (words[word_pos]+(" ")+words[word_pos+1]+(" ")+words[word_pos+2])

        with open("anti_oedipus_chopped.txt", "r") as file:
            data = file.read()
            words = data.split()
      
    # Generating a random number for word position
            word_pos = random.randint(0, len(words)-1)
    
            c= (words[word_pos]+(" ")+words[word_pos+1]+(" ")+words[word_pos+2])

        with open("anti_oedipus_chopped.txt", "r") as file:
            data = file.read()
            words = data.split()
      
    # Generating a random number for word position
            word_pos = random.randint(0, len(words)-1)
    
            d= (words[word_pos]+(" ")+words[word_pos+1]+(" ")+words[word_pos+2])

        with open("anti_oedipus_chopped.txt", "r") as file:
            data = file.read()
            words = data.split()
      
    # Generating a random number for word position
            word_pos = random.randint(0, len(words)-1)
    
            e= (words[word_pos]+(" ")+words[word_pos+1]+(" ")+words[word_pos+2])

        with open("anti_oedipus_chopped.txt", "r") as file:
            data = file.read()
            words = data.split()
      
    # Generating a random number for word position
            word_pos = random.randint(0, len(words)-1)
    
            f= (words[word_pos]+(" ")+words[word_pos+1]+(" ")+words[word_pos+2])

        with open("anti_oedipus_chopped.txt", "r") as file:
            data = file.read()
            words = data.split()
      
    # Generating a random number for word position
            word_pos = random.randint(0, len(words)-1)
    
            g= (words[word_pos]+(" ")+words[word_pos+1]+(" ")+words[word_pos+2])

        with open("anti_oedipus_chopped.txt", "r") as file:
            data = file.read()
            words = data.split()
      
    # Generating a random number for word position
            word_pos = random.randint(0, len(words)-1)
    
            h= (words[word_pos]+(" ")+words[word_pos+1]+(" ")+words[word_pos+2])

        with open("anti_oedipus_chopped.txt", "r") as file:
            data = file.read()
            words = data.split()
      
    # Generating a random number for word position
            word_pos = random.randint(0, len(words)-1)
    
            i= (words[word_pos]+(" ")+words[word_pos+1]+(" ")+words[word_pos+2])

        with open("anti_oedipus_chopped.txt", "r") as file:
            data = file.read()
            words = data.split()
      
    # Generating a random number for word position
            word_pos = random.randint(0, len(words)-1)
    
            j= (words[word_pos]+(" ")+words[word_pos+1]+(" ")+words[word_pos+2])

    aa=("\n")+textwrap.fill(("\n")+a+
    ("\n")+b+
    ("\n")+c+
    ("\n")+d+
    ("\n")+e+
    ("\n")+f+("\n")+g+("\n")+h+("\n")+i+("\n")+j,width=70)
    
def click():

    #stop gate
    if stop == 1:
        global randomvalue
        sentencemaker()
        global startpos1
        global startpos2
        global endpos1
        global endpos2
        global startpos1a
        global startpos2a
        global endpos1a
        global endpos2a
        
        randomvalue=(randint(1,20))
        
        my_text.insert(END,aa)
        my_text.see("end")

        #text postion selection
        startpos1=startpos1+58
        startpos2=startpos2+58
        endpos1=endpos1+68
        endpos2=endpos2+68

        window.after(2000, click)
    elif stop == 0:
        ""

def end():
    global stop
    stop = 0

#buttons
btn = Button(window,text="♥",command=start)
btn.pack(side = BOTTOM)
btn2 = Button(window, text="♠", command=end)
btn2.pack(side=BOTTOM, pady=0)

#window transparent
window.attributes('-alpha',0.5)

#placing cursor is the text area
my_text.focus()

#sustain window
window.mainloop()
