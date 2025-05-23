#python 3.7.9

#This program has a simple function and uses a Tkinter window and button. When you press the button you get two random English words in the text box which can be copied elsewhere.
#To save space on the Github I will not upload the words_alpha.txt file, you can find the same file titled myFile.txt in the Drawing Machine folder on Github.


from tkinter import *
import random

#create window

window = Tk()
window.title("Random Binary Words")
window.configure(background="lightblue")
window.geometry('500x500')

#key down function
def click():
    output.delete(0.0, END)
    try:
        Info = random.choice(open("words_alpha.txt","r",encoding='utf8').read().split())+" " +random.choice(open("words_alpha.txt","r",encoding='utf8').read().split())
    except:
        Info = ("Sorry there is no entry for that number, please try another")    
    output.insert(END,Info)

#create another label for text 'info'
Label (window,text="Random Word Binary:", bg="lightgreen", fg="black", font="none 14 bold") .grid(row=1, column=0, sticky=S, pady = 80)

#create a text box
output= Text(window, width=40, height=5, wrap=WORD, background="white")

output.grid(row=2, column=0, columnspan=1, sticky=S, padx = 90)

#add a submit button
Button(window,text="Pick Random Words",command=click) .grid(row=3, column=0, sticky=S, pady = 20)


window.mainloop()




#add a submit button
Button(window,text="Pick Random Words",command=click) .grid(row=6, column=0, sticky=W)


#create another label for text 'info'
Label (window,text="\nWords:", bg="lightgreen", fg="black", font="none 14 bold") .grid(row=0, column=0, sticky=W)

#create a text box
output= Text(window, width=40, height=5, wrap=WORD, background="white")

output.grid(row=5, column=0, columnspan=2, sticky=W)



window.mainloop()
