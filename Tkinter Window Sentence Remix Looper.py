#python 3.7.9
#This program makes questions that are semi randomized but also changes their colour formatting in the output window, it also runs on a loop for display in a gallery context or for recording it over the top of a video.
#This program needs a myFile.txt which you can download from Drawing Program on Github, it is all the words in the English Dictionary

import random
from tkinter import*
import tkinter.font as tkFont
from tkinter import scrolledtext
from random import randint
import time
import sys
window = Tk()
window.title('Data Stream')
window.geometry("1000x900")
#font
helv36 = tkFont.Font(family="Helvetica",size=30,weight="bold")

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

#textbox
my_text= scrolledtext.ScrolledText(window, width=58, height=18, font=(helv36),fg='lime green')

#pack to window
my_text.pack(pady=20)

#start variables
startpos1=1
startpos2=50

endpos1=51
endpos2=100

#start variables for second text highlighter

startpos1a=101
startpos2a=150

endpos1a=151
endpos2a=200



def sentencemaker():
    global aa
    a=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    b=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    aa=("How do we use science fiction and the ")+a+(" to be more speculative about the ")+b+("?")
    
#list
aa = "help"

#number = sample(range(1,5), 1)
def click():
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
                 
    '''newlist1 = []    
        
    newlist1.append( random.sample(relax,k= randomvalue))
    
    newlist1.append( random.sample(relax,k= randomvalue))
    
    newlist1.append( random.sample(relax,k= randomvalue))

    for item in newlist1:
        listtostr = item'''

    my_text.insert(END,aa)
    my_text.see("end")
    highlight_text(tag_name='tag1', lineno=1, start_char=randint(startpos1,startpos2), end_char=randint(endpos1,endpos2), fg_color='red')
    highlight_text(lineno=1, start_char=randint(startpos1a,startpos2a), end_char=randint(endpos1a,endpos2a), bg_color="black", fg_color='yellow', tag_name='zingo')

    startpos1=startpos1+58
    startpos2=startpos2+58
    endpos1=endpos1+68
    endpos2=endpos2+68
    
    startpos1a=startpos1a+48
    startpos2a=startpos2a+48
    endpos1a=endpos1a+58
    endpos2a=endpos2a+58
    window.after(2000, click)

#crazy color stuff
def highlight_text(tag_name, lineno, start_char, end_char, bg_color=None, fg_color=None):
    my_text.tag_add(tag_name, f'{lineno}.{start_char}', f'{lineno}.{end_char}')
    my_text.tag_config(tag_name, background=bg_color, foreground=fg_color)

  
#add a submit button
btn = Button(window,text="♥",command=click)
btn.pack(side = LEFT)

#window transparent
window.attributes('-alpha',0.5)
#placing cursor is the text area
my_text.focus()

#sustain window
window.mainloop()
