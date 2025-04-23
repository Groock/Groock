from tkinter import *
import random
from random import randint
from PIL import Image, ImageDraw, ImageTk

#python 3.7.9

#This program creates random drawing-collages in a Tkinter window, it pulls random words from English dictionary text file and randomizes the gif images on screen.
#♥ Button to start, ♠ Button to finish the drawing, X Button clears the canvas to start over again.
#This program requires myFile.txt which is the English dictionary file.
#Also required are .gif files: fractal Fractalfrag4 Fractalfrag5 which are images of my 3D CGI artworks.

root = Tk()
root.title('Canvas')
root.geometry('1200x800')

my_canvas = Canvas(root, width=1200, height=700, bg="white")
my_canvas.pack(pady=20)

# Read the Image
image = Image.open("fractal.gif")
image2 = Image.open("Fractalfrag4.gif")
image3 = Image.open("Fractalfrag5.gif")

#random sizes

def randomsizes():
    global randomsize1
    global randomsize2
    global randomsize3
    global randomsize4

    global img
    global img2
    global img3
    
    randomsize1 = randint(10, 1000)
    randomsize2 = randint(10, 1000)
    randomsize3 = randint(10, 1000)
    randomsize4 = randint(10, 1000)

    # Reszie the image using resize() method
    resize_image = image.resize((randomsize1, randomsize2))
    resize_image2 = image2.resize((randomsize3, randomsize4))
    resize_image3 = image3.resize((randomsize3, randomsize1))

    img = ImageTk.PhotoImage(resize_image)
    img2 = ImageTk.PhotoImage(resize_image2)
    img3 = ImageTk.PhotoImage(resize_image3)

#variables

stop = 1

images = []  # to hold the newly created image(s)        

def create_rectangle(x1, y1, x2, y2, **kwargs):
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = img
        images.append(ImageTk.PhotoImage(image))
        my_canvas.create_image(x1, y1, image=images[-1], anchor='nw')
    my_canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

def randcords():
    global x1
    global x2
    global y1
    global y2
    x1 = randint(1, 1200)
    x2 = randint(1, 1200)
    y1 = randint(1, 700)
    y2 = randint(1, 700)

def start():
    global stop
    stop = 1
    create()

# my_canvas.create_line(x1,y1,x2,y2, fill="color")
def create():
    randomsizes()
    randcords()
    my_canvas.create_arc(x1, y1, x2, y2, fill="")
    randcords()
    my_canvas.create_image(x1, y1, image = img)
    randcords()
    my_canvas.create_image(x1, y1, image = img2)
    randcords()
    my_canvas.create_image(x1, y1, image = img3)
    randcords()
    randomtext=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    my_canvas.create_text(x1,y1,fill="black",font="Helvetica 20 italic",
                        text=randomtext)
    randcords()
    my_canvas.create_line(x1, y1, x2, y2, fill="white")
    randcords()
    my_canvas.create_oval(x1, y1, x2, y2, fill="")
    #new polygon
    #create_rectangle(x1, y1, x2, y2, fill="white", alpha=0.2)

    if stop == 1:
        root.after(50, create)
    elif stop == 0:
        ""
    
def end():
    global stop
    stop = 0

def clear():
    my_canvas.delete("all")

# add the button
btn = Button(root, text="♥", command=start)
btn.pack(side=LEFT, pady=0)
btn2 = Button(root, text="♠", command=end)
btn2.pack(side=LEFT, pady=0)
btn3 = Button(root, text="X", command=clear)
btn3.pack(side=LEFT, pady=0)

root.mainloop()
