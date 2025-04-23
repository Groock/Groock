#from tkinter import *
import tkinter
import random
from random import randint
from PIL import Image, ImageDraw, ImageTk
from canvas_functions import *
import os
#from web_cam import *

#Python 3.7.9

#This program is a more stylized drawing machine in a Tkinter window. It has a button function called Life-Death ♣ that can advance the drawing by one step at a time.
#This program creates random lines, shapes and utilizes a python generated Mandelbrot image, with same gradient images also.
#This program requires the following in the same folder: myFile.txt SaveTestRenamed.gif box.png
#This program also requires python files: canvas_functions.py and web_cam.py (web_cam.py uses cv2 to input a webcam image into the drawing program, but may not be fully implemented)

"""
I am making this program as emergent, it is emerging from the plane between my mind and itself as i make it, it is also making itself,
others have made it also, it has been made by nature, by the plane of the universe.
This program is a drawing machine,
it draws on the screen.
A 3D print told me something, that this was important to the practice, to the coninuing work, the mork must be done to find out what
must be done and what must be done is the work. The machine works on me. Work is being done.
"""

roottk = tkinter.Tk()

roottk.title('"We must die as egos and be born again in the swarm, not separate and self-hypnotized, but individual and related."')

roottk.geometry('1200x900')

#roottk.iconphoto(True, mainbackpic)

#background image on canvas

#create image
background_image = tkinter.PhotoImage(file='box.png')

#create a label
back_label = tkinter.Label(roottk, image = background_image)

back_label.place(x=0, y=0, relwidth=1, relheight=1)

#roottk.tk.call('wm', 'iconphoto', root._w, img)

#unused code

#background_canvas = tkinter.Canvas(roottk, width = 200, height = 200, bg = 'cyan')

#background_canvas.create_image((500, 500), image = mainbackpic)

#background_canvas.pack(expand=1)

#frame container for all widgets

frame = tkinter.Frame(roottk, relief=None, borderwidth=None, bg='burlywood')

frame.pack(expand=1)

#nope
#label1 = tkinter.Label( roottk, image = mainbackpic)
#label1.place(x = 0, y = 0)


 

#drawing canvas variables

canvasw = 1200
canvash = 800

#drawing canvas

my_canvas = tkinter.Canvas(frame, width=canvasw, height=canvash, bg="burlywood", highlightthickness=0)

my_canvas.pack(pady=0)



# Read the Image and create as variables
image = Image.effect_mandelbrot((1000,1000),(0,0,1,1), 100)
image2 = Image.effect_noise((100,100),10)
image3 = Image.radial_gradient('1')
image4 = Image.open("SaveTestRenamed.gif")

#random sizes

def randomsizes():
    global randomsize1
    global randomsize2
    global randomsize3
    global randomsize4

    global img
    global img2
    global img3
    global img4
    
    randomsize1 = randint(10, 1000)
    randomsize2 = randint(10, 1000)
    randomsize3 = randint(10, 1000)
    randomsize4 = randint(10, 1000)

    # Reszie the image using resize() method
    resize_image = image.resize((randomsize1, randomsize2))
    resize_image2 = image2.resize((randomsize3, randomsize4))
    resize_image3 = image3.resize((randomsize3, randomsize1))
    resize_image4 = image4

    img = ImageTk.PhotoImage(resize_image)
    img2 = ImageTk.PhotoImage(resize_image2)
    img3 = ImageTk.PhotoImage(resize_image3)
    img4 = ImageTk.PhotoImage(resize_image4)

#variables

stop = 1

images = []  # to hold the newly created image(s)        

def create_rectangle(x1, y1, x2, y2, **kwargs):
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = roottk.winfo_rgb(fill) + (alpha,)
        image = img
        images.append(ImageTk.PhotoImage(image))
        my_canvas.create_image(x1, y1, image=images[-1], anchor='nw')
    my_canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

def randcords():
    global x1
    global x2
    global y1
    global y2
    x1 = randint(1, canvasw)
    x2 = randint(1, canvasw)
    y1 = randint(1, canvash)
    y2 = randint(1, canvash)

def start():
    global stop
    stop = 1
    create()

def start1step():
    global stop
    stop = 0
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

    if stop == 1:
        roottk.after(50, create)
    elif stop == 0:
        #web cam image from file displayed
        randcords()
        my_canvas.create_image(x1, y1, image = img4)
        return
    
def end():
    global stop
    stop = 0

def clear():
    my_canvas.delete("all")

def colour_average_start():
    
    #delete file
    global image4
    #clear image variable
    image4 = 0
    #os.remove('SaveTestRenamed.gif')
    
    #reoen image after cam func
    image4 = Image.open("SaveTestRenamed.gif")
    save_frame
    

# pack and add the buttons
btn = tkinter.Button(frame, text="Life ♥", activebackground='green', foreground='dark orchid', background='burlywood', width=None, bd=16, height=None, font="Helvetica 20 italic", command=start)
btn.pack(side=tkinter.LEFT, pady=5, padx=3)
btn2 = tkinter.Button(frame, text="Death ♠", activebackground='red', foreground='dark orchid', background='burlywood', bd=16, font="Helvetica 20 italic", command=end)
btn2.pack(side=tkinter.LEFT, pady=2)
btn3 = tkinter.Button(frame, text="Reset Immanence ♦", activebackground='blue', foreground='dark orchid', background='burlywood', bd=16, font="Helvetica 20 italic", command=clear)
btn3.pack(side=tkinter.LEFT, pady=2)
btn4 = tkinter.Button(frame, text="Life-Death ♣", activebackground='yellow', foreground='dark orchid', background='burlywood', bd=16, font="Helvetica 20 italic", command=start1step)
btn4.pack(side=tkinter.LEFT, pady=2)
btn5 = tkinter.Button(frame, text="Self Reflection ☺_!_!_!_!_!_!_!", activebackground='white', foreground='dark orchid', background='burlywood', bd=16, font="Helvetica 20 italic", command=colour_average_start)
btn5.pack(side=tkinter.LEFT, pady=2)



roottk.mainloop()
