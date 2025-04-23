
#python 3.7.9
#Hashtag mixer program that uses a list instead of a text file, This is a result of experimentation with different ways of storing the hashtag data.

from tkinter import *
import random

#list
lst=["#2001aspaceodyssey","#3dart","#3dartist","#3ddigitalrender","#3dmodel","#3dmodeling","#3dprinting","#3drender","#3dscan","#Absence","#Abstract","#Abstractart","#Abstractgeometry","#Abstraction","#Abstractlandscape","#Abstractworld","#Acrylicart","#Acrylicpainting","#Aesthetic","#Arthistory","#Artist","#Artistsofinstagram","#Artstudio","#Beautifulbizarre","#Blender28","#Blenderart","#Blendercommunity","#Bristol","#Bristolart","#Bristolgallery","#Callforartists","#Cgjung","#Culture","#Collage","#Collagestash","#Collectgraphics","#Conceptual","#Conceptual_Art","#Conceptualart","#Contemporaryart","#Contemporarypainting","#Contemporaryphotography","#Contemporarysculpture","#Covid19art","#Cyberart","#Cyberspace","#Cyberwave","#Cyclesrender","#Dada","#Databending","#Digitalart","#Digitalartist","#Digitalcollage","#Emergingartist","#Entropy","#Existentialart","#Fineartpractice","#Freeonlinegallery","#Freeonlinespace","#Freevirtualgallery","#Futureart","#Geometricabstraction","#Georgepeterthom","#Glitchaesthetic","#Glitchart","#Glitchartist","#Glitchartistscollective","#Glitchcult","#Glitche","#Glitched","#Grafiktrafik","#Graphics","#History","#Ig_Underground","#Installation","Independentgallery","#Installationart","#Internetart","#Kitsch","#Latecapitalism","#Lensculturediscovery","#Linedrawing","#Minimalart","#Minimalartist","#Minimalismart","#Misunderstoodplace","#Modernart","#Moderngallery","#Mythology","#Netart","#Humans","#Newaesthetic","#Newmediaart","#Onlineart","#Onlinegallery","#Opart","#Opticalart","#Painting","#Photography","#Photorealism","#Phygital","#Poliigon","#Postinternet","#Postminimalism","#Postmodern","#Postmodernart","#Postmoderngallery","#Primitivism","#Provocation","#Readymade","#Realitycapture","#Reflectontheworld","#Refracting","#Rendering","#Renderzone","#Retrowaveaesthetic","#Retrowaveart","#Science","#Scifilandscape","#Space","#Spaceart","#Spacesofthefuture","#Surreal","#Surrealist","#Synthwave","#Techno","#Tinyroom","#Trance","#Underground","#Underworld","#Vaporwave","#Vaporwaveaesthetic","#Vaporwaveart","#Vaporwavevibes","#Virtualarchive","#Virtualart","#Virtualenvironment","#Virtualgallery","#Virtualmuseum","#Virtualsculpturepark","#Virtualspaceforartists","#Visualmeditation","#Webpunk"]

#key down function
def click():
    output.delete(0.0, END)
    try:
        Info = random.sample(lst,k=30)
    except:
        Info = ("Sorry there is no entry for that number, please try another")    
    output.insert(END,Info)

#create window

window = Tk()
window.title("Hashtag Mixer")
window.configure(background="white")


label = Label (window,text="Hashtags", bg="white") .grid(row=0, column=0, sticky=N)

#add a submit button
Button(window,text="Submit",command=click) .grid(row=3, column=0, sticky=W)

#create another label for text 'info'
Label (window,text="\nInfo:", bg="white", fg="black", font="none 10 bold") .grid(row=4, column=1, sticky=W)

#create a text box
output= Text(window, width=70, height=8, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

window.mainloop()
