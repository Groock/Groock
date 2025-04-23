#python 3.7.9

#Unfinished project, RPG game played into Tkinter window with map navigation, inventory, goblins with health points and attack and so on.


import tkinter as tk
from tkinter import *
import random

#1 adventure mode, 0 combat mode, 2 adventure inventory, 3 combat inventory
gamemode=1

#current map position A+N B+W A-S B-E
mappos=[0,0]

#dict to store all locations with the co-ordinates as the Key: and numbered Key of the locations as the :Value
dict = { (0,0):'1' }

#current location Key number
locationnumber = ('1')

globallocation = 1

globallocationkey = None

vector = (0,0)

class Game():
    def __init__(self):
        
        self.root = tk.Tk()

        self.root.title('Generick Science Fiction RPG')
        
        self.database = {}
        
        self.locations = {'1':'You walk into a wooded area.','2':'You walk over a rocky moorland.',
                          '3':'You walk into a stream.','4':'You walk into a goblin nest.',
                          '5':'You walk through a wet cave.','6':'You walk up a large hill and into a valley.',
                          '7':'You walk into a clearing in a forest.','8':'You walk close to a treacherous bog.',
                          '9':'You walk over a mountain pass.','10':'You walk over a dune savanna.',
                          '11':'You walk to the edge of seeming endless plains.','12':'You walk over a dried riverbed.',
                          '13':'You stumble into a small settlement.','14':'You walk near a derlict fortress.',
                          '15':'You walk past an active volcano.','16':'You enter into a dense jungle.',
                          '17':'You walk through a dry scrubland.','18':'You walk around a huge crater.',
                          '19':'You walk near to a rebel base.','20':'You spot a council of Urnker supply depot.'}
        
        #combat mode is 0, adventute mode is 1, adventure inventory mode is 2, combat inventory is 3, starting off in adventure mode untill finding goblin.
        
        self.d20 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
        self.d6 =['1','2','3','4','5','6']
        
        #initial buttons
        self.btn1 = tk.Button(self.root, text='Walk North', command=self.walknorth)
        self.btn2 = tk.Button(self.root,text='Walk East',command=self.walkeast)
        self.btn3 = tk.Button(self.root,text='Walk South',command=self.walksouth)
        self.btn4 = tk.Button(self.root,text='Walk West',command=self.walkwest)
        self.btnengage = tk.Button()
        self.btn5 = tk.Button(self.root, text='Open Inventory', command=self.adventureinventory)
        
        #text box
        self.text_box = tk.Text (self.root, font = 20, height = 21, width = 45)
    
        #label text init
        self.label1text = tk.StringVar()
    
        self.label1 = tk.Label(self.root,textvariable=self.label1text)
        
        self.text_box.pack()
        self.btn1.pack()
        self.btn2.pack()
        self.btn3.pack()
        self.btn4.pack()
        self.btnengage.pack()
        self.btn5.pack(side=tk.LEFT)
        self.label1.pack()
        #tk window loop
        self.root.mainloop()
    
    def creategoblin(self):
        self.goblin = {"HP":50, "Attack":5}
    
    def attack(self):
        self.text_box.delete('1.0','50.0')
        self.damage = random.choice(self.d20)
        self.text_box.insert('1.0','Attacked Goblin with sword, for '+self.damage+' damage.')
    
    def defend(self):
        self.dam=random.choice(self.d20)
        self.text_box.delete('1.0','50.0')
        self.text_box.insert('1.0','Defended against attack for '+self.dam+' damage.')
    
    def special(self):
        self.text_box.delete('1.0','50.0')
        self.text_box.insert('1.0', 'Special Not Unlocked Yet')
        
    def rolld20(self):
        #roll a 20 sided dice
        return random.choice(self.d20)
    
    def location(self):
        #assign a random location to the players current locaton
        global globallocation
        global locationnumber
        locationnumber=self.rolld20()
        globallocation=self.locations[locationnumber]
        #globallocationkey=self.locations[globallocation]
        return globallocation

    def getcurrentposn(self):
        #get current position of player and save it to the dictionary if an entry doesn't already exist
        global vector
        self.axisA = mappos[0]
        self.axisB = mappos[1]
        vector = self.axisA,self.axisB
        self.text_box.insert(END,' Current Vector is: ')
        self.text_box.insert(END,vector)
        Boolean1 = vector in dict
        if Boolean1 is False:
                dict[vector] = locationnumber
        else:
                return

    def walknorth(self):
        global mappos
        mappos[0] = mappos[0]+1
        self.text_box.delete('1.0','50.0')
        localdescription=self.location()
        self.text_box.insert('1.0',' After heading 50 meters into the North for some time. '+localdescription)
        self.text_box.insert(END,' <^Grid position^> ')
        self.text_box.insert(END,mappos)
        self.getcurrentposn()
        if localdescription==('You walk into a goblin nest.'):
                self.text_box.insert('50.0',' Oh god no!')
                self.btnengage.configure(text='Engage Enemy', command=self.returnCombat)
        else:
                self.text_box.insert('80.0',' Where to next?')
            
    def walkeast(self):
        global mappos
        mappos[1] = mappos[1]+1
        self.text_box.delete('1.0','50.0')
        self.text_box.insert('1.0','After exploring 50 meters East for some time. '+self.location())
        self.text_box.insert(END,' <^Grid position^> ')
        self.text_box.insert(END,mappos)
        self.getcurrentposn()
    
    def walksouth(self):
        global mappos
        mappos[0] = mappos[0]-1
        self.text_box.delete('1.0','50.0')
        self.text_box.insert('1.0','After treking 50 meters South for some time. '+self.location())
        self.text_box.insert(END,' <^Grid position^> ')
        self.text_box.insert(END,mappos)
        self.getcurrentposn()
    
    def walkwest(self):
        global mappos
        mappos[1] = mappos[1]-1
        self.text_box.delete('1.0','50.0')
        self.text_box.insert('1.0','After trailing 50 meters Westward for some time. '+self.location())
        self.text_box.insert(END,' <^Grid position^> ')
        self.text_box.insert(END,mappos)
        self.getcurrentposn()
    
    def returnAdventure(self):
        global gamemode
        gamemode = 1
        self.changeButton()
    
    def returnCombat(self):
        global gamemode
        gamemode = 0
        self.changeButton()
    
    def adventureinventory(self):
        global gamemode
        gamemode = 2
        
        self.text_box.insert('1.0','Opened inventory')
        self.text_box.delete('1.0','50.0')
        self.text_box.insert('10.0',gamemode)
        self.changeButton()
    
    def combatinventory(self):
        global gamemode
        gamemode=3
        self.changeButton()
    
    def useitem(self):
        self.text_box.delete('1.0','50.0')
        self.text_box.insert('1.0','Used item')

    def createmapimage(self):
        can = \
        Canvas(self.root, height = 100, width = 100, bg = 'green')
        can.create_image(10, 50)
        can.create_line(0,0,100,100, width = 25, fill = 'yellow')
        can.pack( side = RIGHT, padx = 2, pady = 2 )

    def map(self):
        self.text_box.delete('1.0','50.0')
        self.text_box.insert('1.0',dict)
        self.createmapimage()
                

    def changeButton(self):
####
        #adventure mode
        if gamemode == 1:
            #set buttons
            self.btn1.configure(text='Walk North', command=self.walknorth)
            self.btn2.configure(text='Walk East', command=self.walkeast)
            self.btn3.configure(text='Walk South', command=self.walksouth)
            self.btn4.configure(text='Walk West', command=self.walkwest)
            self.btn5.configure(text='Inventory', command = self.adventureinventory)
####    
        #combat mode 
        elif gamemode == 0:
            
            self.btn1.configure( text="Attack", command=self.attack)
            self.btn2.configure( text="Defend", command=self.defend)
            self.btn3.configure( text="Special", command=self.special)
            self.btn4.configure( text="Run Away", command=None)
            self.btn5.configure( text = "Inventory", command = self.combatinventory)

####    
        #adventure inventory
        
        elif gamemode == 2:
            
            self.btn1.configure(text="Use item",command=self.useitem)
            self.btn2.configure( text="Item Up", command=None)
            self.btn3.configure(text="Item Down", command=None)
            self.btn4.configure(text="Map", command=self.map)
            self.btn5.configure( text= "Exit Inventory", command = self.returnAdventure)
            
####
        #combat inventory
        elif gamemode == 3:
            
            self.btn1.configure(text="Use item",command=self.useitem)
            self.btn2.configure( text="Item Up", command=None)
            self.btn3.configure(text="Item Down", command=None)
            self.btn4.configure(text="Combat Map", command=None)
            self.btn5.configure( text= "Exit Inventory", command = self.changeButton)
        
        else:
            self.text_box.insert('error')
        self.btn1.pack()
        self.btn2.pack()
        self.btn3.pack()
        self.btn4.pack()
        self.btn5.pack()

app=Game()
