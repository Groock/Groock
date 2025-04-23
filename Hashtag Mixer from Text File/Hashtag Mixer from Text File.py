#Python 3.7.9

# A hashtag mixer for instagram art content posts. The program creates a Tkinter window, submit is pressed to generate 30 random hashtags from the sample file, this uses a text file as it's data source, radio buttons were an intended feature to select from curated data sets.
#This program requires file: hashtags.txt

from tkinter import *
import random

#open txt file
file = open('hashtags.txt','r')

#how many lines do we have? File reading and closing

def filelength():
    filelength = 0

    for line in file:
        filelength = filelength+1
    print (("File line length: ")+str(filelength))
    return filelength
    

hashtaglist = file.read().splitlines()

print (hashtaglist)
print (filelength())

file.close()

#create window

window = Tk()
window.title("Humanartist Hashtag Mixer")
window.configure(background="white")

#create selection variable
selection=StringVar()

#removed words
'''"#Acrylicart""#Aesthetic"'''
'''"#Acrylicpainting"'''
'''"#Cgjung"'''
'''"#Callforartists"'''
'''"#Contemporarysculpture"'''
'''"#Collagestash"'''
'''"#Contemporarypainting"'''
'''"#Bristolgallery"'''
'''"#Contemporaryphotography"'''
'''"#Cyberwave"'''
'''"#Glitchartistscollective"'''
'''"#Glitche","#Glitched"'''
'''"#Freeonlinegallery"'''
'''"#Glitchaesthetic"'''
'''"#Freevirtualgallery"'''
'''"#Vaporwaveaesthetic"'''
'''"#Onlinegallery",'''
'''"#Vaporwaveart"'''
'''"#Vaporwavevibes"'''
'''"#Virtualspaceforartists"'''
'''"#Virtualsculpturepark"'''
'''"#Vaporwave"'''

#key down function
def click():
    output.delete(0.0, END)
    try:
        #get random list and save as info
        Info = random.sample(hashtaglist,k=30)
        
        #make all words into lowercase
        for i in range(len(Info)):
            Info[i]=Info[i].lower()
            
        #sort alphabetically
        Sorted = sorted(Info)

        """
        #initialize an empty string
        EmptyString = " "
        #join list to string
        JoinedString = EmptyString.join(Info)
        #Convert String to List        
        Words = JoinedString.split(" ")
        #
        """
        #make list into string and remove trash characters
        sortedasstring = (' '.join(map(str,Sorted)))
        
    except(NameError , IndexError ) as msg :
         
        Info = ("Sorry there is no entry for that number, please try another"+msg)
        
    output.insert(END,sortedasstring)

label = Label (window,text="Hashtags", bg="white") .grid(row=0, column=0, sticky=N)

#radio buttons for selection
radio_1 = Radiobutton(window, text='Default', variable=selection, value='Default Hashtags')
radio_2 = Radiobutton(window, text='3D Model', variable=selection, value='3D Hashtags')
radio_3 = Radiobutton(window, text='2D Image', variable=selection, value='2D Hashtags')

radio_1.select()

radio_1.grid(row=1, column=0, sticky=W)
radio_2.grid(row=2, column=0, sticky=W)
radio_3.grid(row=3, column=0, sticky=W)

#add a submit button
Button(window,text="Submit",command=click) .grid(row=4, column=0, sticky=W)

#create another label for text 'info'
Label (window,text="\nInfo:", bg="white", fg="black", font="none 10 bold") .grid(row=4, column=1, sticky=W)

#create a text box
output= Text(window, width=70, height=8, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

window.mainloop()
