# import required module
from tkinter import*
import tkinter.font as tkFont
import random
import time
import linecache
import textwrap

#Python 3.7.9

#This program generates sentences in a transparent TK Window that say the government has promised this and that.
#This program requires text file called myFile.txt to be present in the same folder which is the International Paris Agreement on Climate Change

#tk window
window = Tk()
#font
helv36 = tkFont.Font(family="Helvetica",size=30,weight="bold")
#window title
window.title('Remixed Unitied Nations Paris Climate Agreement')
#import pyautogui
loop = 1
#inital button
activate = Button( window )

#fixed sentences variables
govtext1=StringVar()
govtext2=StringVar()
govtext3=StringVar()
govtext4=StringVar()
govtext5=StringVar()
govtext6=StringVar()
#fixed sentences column 2
govtext7=StringVar()
govtext8=StringVar()
govtext9=StringVar()
govtext10=StringVar()
govtext11=StringVar()
govtext12=StringVar()

#start string variable class
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
f=StringVar()
g=StringVar()
h=StringVar()
i=StringVar()
j=StringVar()
k=StringVar()
l=StringVar()
#set the fixed text
govtext1.set("The government has promised")
govtext2.set("The government has promised")
govtext3.set("The government has promised")
govtext4.set("The government has promised")
govtext5.set("The government has promised")
govtext6.set("The government has promised")
#set the fixed text 2
govtext7.set("and")
govtext8.set("and")
govtext9.set("and")
govtext10.set("and")
govtext11.set("and")
govtext12.set("and")
#inital text boxes
a.set("Start")
b.set("Start")
c.set("Start")
d.set("Start")
e.set("Start")
f.set("Start")
g.set("Start")
h.set("Start")
i.set("Start")
j.set("Start")
k.set("Start")
l.set("Start")
#width label
sizeframe = Label (window)
sizeframe2 = Label (window)
#fixed text label variables
govtextbox1= Label( window, padx=1, textvariable=(govtext1), font=helv36)
govtextbox2= Label( window, padx=1, textvariable=(govtext2), font=helv36)
govtextbox3= Label( window, padx=1, textvariable=(govtext3), font=helv36)
govtextbox4= Label( window, padx=1, textvariable=(govtext4), font=helv36)
govtextbox5= Label( window, padx=1, textvariable=(govtext5), font=helv36)
govtextbox6= Label( window, padx=1, textvariable=(govtext6), font=helv36)
#column 2
govtextbox7= Label( window, padx=1, textvariable=(govtext7), font=helv36)
govtextbox8= Label( window, padx=1, textvariable=(govtext8), font=helv36)
govtextbox9= Label( window, padx=1, textvariable=(govtext9), font=helv36)
govtextbox10= Label( window, padx=1, textvariable=(govtext10), font=helv36)
govtextbox11= Label( window, padx=1, textvariable=(govtext11), font=helv36)
govtextbox12= Label( window, padx=1, textvariable=(govtext12), font=helv36)

#labels tk
wordbox1 = Label ( window, padx=1, textvariable=(a), font=helv36)
wordbox2 = Label ( window, padx=1, textvariable=(b), font=helv36)
wordbox3 = Label ( window, padx=1, textvariable=(c), font=helv36)
wordbox4 = Label ( window, padx=1, textvariable=(d), font=helv36)
wordbox5 = Label ( window, padx=1, textvariable=(e), font=helv36)
wordbox6 = Label ( window, padx=1, textvariable=(f), font=helv36)
wordbox7 = Label ( window, padx=1, textvariable=(g), font=helv36)
wordbox8 = Label ( window, padx=1, textvariable=(h), font=helv36)
wordbox9 = Label ( window, padx=1, textvariable=(i), font=helv36)
wordbox10 = Label ( window, padx=1, textvariable=(j), font=helv36)
wordbox11 = Label ( window, padx=1, textvariable=(k), font=helv36)
wordbox12 = Label ( window, padx=1, textvariable=(l), font=helv36)
#width label
sizeframe.grid(row=1,column=3,padx=52)
sizeframe2.grid(row=1,column=5,padx=52)
#tk gov text positions
govtextbox1.grid(row =1,column=2)
govtextbox2.grid(row =2,column=2)
govtextbox3.grid(row =3,column=2)
govtextbox4.grid(row =4,column=2)
govtextbox5.grid(row =5,column=2)
govtextbox6.grid(row =6,column=2)
#tk gov text positions column 2
govtextbox7.grid(row =1,column=5)
govtextbox8.grid(row =2,column=5)
govtextbox9.grid(row =3,column=5)
govtextbox10.grid(row =4,column=5)
govtextbox11.grid(row =5,column=5)
govtextbox12.grid(row =6,column=5)
#tk label positions
wordbox1.grid(row = 1, column = 3, columnspan = 2, padx = 10)
wordbox2.grid(row = 2, column = 3, columnspan = 2)
wordbox3.grid(row = 3, column = 3, columnspan = 2)
wordbox4.grid(row = 4, column = 3, columnspan = 2)
wordbox5.grid(row = 5, column = 3, columnspan = 2)
wordbox6.grid(row = 6, column = 3, columnspan = 2)
wordbox7.grid(row = 1, column = 6, columnspan = 2)
wordbox8.grid(row = 2, column = 6, columnspan = 2)
wordbox9.grid(row = 3, column = 6, columnspan = 2)
wordbox10.grid(row = 4, column = 6, columnspan = 2)
wordbox11.grid(row = 5, column = 6, columnspan = 2)
wordbox12.grid(row = 6, column = 6, columnspan = 2, padx =10)
#button
activate.grid(row = 1, column = 1)

# print random word
def click():

    a.set(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    b.set(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    c.set(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    d.set(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    e.set(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    f.set(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    g.set(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    h.set(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    i.set(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    j.set(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    k.set(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    l.set(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    #m=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    #n=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    #o=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    #p=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    #q=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    #r=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    #s=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    #t=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))

    #aa=("How do we use science fiction and the ")+a+(" to be more speculative about the ")+b+("?")#+c+(" ")+d+(" ")+e+(" ")+f+(" ")+g+(" ")+h+(" ")+i+(" ")+j+(" ")+k+(" ")+l+(" ")+m+(" ")+n+(" ")+o+(" ")+p+(" ")+q+(" ")+r+(" ")+s+(" ")+t
    """aa=textwrap.fill((" As an art pyschotherapist and artist focusing on ")+a+
    (", George Thom intends to make visible the ")+b+
    (" and ")+c+
    (". The role of the image in determining ")+d+
    (" has a long history, technologies of ")+e+
    (" have shaped ")+f+(". George seeks to address questions of ")+g+(", ")+h+(" and ")+i+(". "),width=70)#+j+(" ")+k+(" ")+l+(" ")+m+(" ")+n+(" ")+o+(" ")+p+(" ")+q+(" ")+r+(" ")+s+(" ")+t
#pyautogui.mouseInfo()
    pyautogui.moveTo(996,986, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(997,934, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(13,125, duration=0.5)
    pyautogui.drag(900,5,duration=0.5)"""

    #print (aa)
    #time.sleep(1)
#button command
activate.configure( text = 'Change',command=click )
#window transparent
window.attributes('-alpha',0.5)
#sustain window
window.mainloop()

