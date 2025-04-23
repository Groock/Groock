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

#list
relax = ['▄','▒','░','╿','✉','☠',
         '☰','☱','☲','☳','☴','☵','☶','☷',
         '♠','♡','♢','♣','♤','♥','♦','♧','♤',
         '✈','✌','✍',
         '➳','❃','❄','❅','❆','❇',
         '❍','❏','❐','❑','❒','❖',
         '✞','✇','✆','✄','♛','♘','✿','☁','☮','☎']
#number = sample(range(1,5), 1)
def click():
    global randomvalue
    
    global startpos1
    global startpos2
    global endpos1
    global endpos2
    global startpos1a
    global startpos2a
    global endpos1a
    global endpos2a
    
    randomvalue=(randint(1,20))
                 
    newlist1 = []    
        
    newlist1.append( random.sample(relax,k= randomvalue))
    
    newlist1.append( random.sample(relax,k= randomvalue))
    
    newlist1.append( random.sample(relax,k= randomvalue))

    for item in newlist1:
        listtostr = item

    string=' '.join(listtostr)

    my_text.insert(END,string)
    my_text.see("end")
    highlight_text(tag_name='tag1', lineno=1, start_char=randint(startpos1,startpos2), end_char=randint(endpos1,endpos2), fg_color='red')
    highlight_text(lineno=1, start_char=randint(startpos1a,startpos2a), end_char=randint(endpos1a,endpos2a), bg_color="black", fg_color='yellow', tag_name='zingo')

    startpos1=startpos1+18
    startpos2=startpos2+18
    endpos1=endpos1+18
    endpos2=endpos2+18
    
    startpos1a=startpos1a+18
    startpos2a=startpos2a+18
    endpos1a=endpos1a+18
    endpos2a=endpos2a+18




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
