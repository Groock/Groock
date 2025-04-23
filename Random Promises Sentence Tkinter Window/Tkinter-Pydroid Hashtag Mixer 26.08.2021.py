import tkinter as tk
import random

#This program can be used on android python on moto5GS device specifically on pydroid. May work on others not tested.
#The program mixes hashtags in a Tkinter window with different buttons for different genres of artwork. It mostly saves me time picking the hashtags myself, and I have limited evidence that this is in any way useful or advantageous on instgram.

root = tk.Tk()

def random_mix_groocks():
	text_box.delete('1.0','50.0')
	mixed = random.sample(hashtags_groocks, k=28)
	for x in mixed:

	#string_mix = ''.join(mixed)
		text_box.insert('1.0',  x + ' ')
	btn_text1.set("Mix Groocks Again")

def random_mix_digital():
	text_box.delete('1.0','50.0')
	mixed = random.sample(hashtags_digital, k=25)
	for x in mixed:

	#string_mix = ''.join(mixed)
		text_box.insert('1.0',  x + ' ')
	btn_text2.set("Mix Digital Again")

def random_mix_physical():
	text_box.delete('1.0','50.0')
	mixed = random.sample(hashtags_physical, k=25)
	for x in mixed:

	#string_mix = ''.join(mixed)
		text_box.insert('1.0',  x + ' ')
	btn_text3.set("Mix Physical Again")

def random_mix_phygital():
	text_box.delete('1.0','50.0')
	mixed = random.sample(hashtags_phygital, k=25)
	for x in mixed:

	#string_mix = ''.join(mixed)
		text_box.insert('1.0',  x + ' ')
	btn_text4.set("Mix Phygital Again")

		
def copy ():
	root.clipboard_clear()
	root.clipboard_append(text_box.get('1.0','50.0'))
	root.update()

hashtags_groocks = ["#2Dart","#3Dart","#3Ddesign","#3ddigitalrender","#3dmodel","#3dscans","#relationalaesthetics","#artistsofinstagram",
                    "#artstudio","#blender","#Bristol","#Bristolart","#Bristolgallery","#Bristolprogramming","#callforart","#collage","#conceptualart","#contemporaryart",
                    "#contemplation","#cyberpunk","#cyberart","#cybernetic","#cyborg","#cyborgmysticism","#cyborgsofinstagram","#cyclesrender","#deepdream","#digitalartist","#digitalart","#digitalcollage",
                    "#dreamworld","#experimentalart","#fineartpractice","#futureutopia","#gallery","#glitchart","#glitchartistscollective",
                    "#graphics","#groocksgallery","#hyperactivity","#hyperconceptual","#internet","#internetart","#modernart","#mythology","#minimalart","#minimalismart","#netart","#neuralart",
                    "#neuralnetworks","#newcontemporary","#newmedia","#newmediaart","#opart","#opticalart","#opencall","#opencallforartists","#postconceptual","#posthuman","#postinternet","#postinternetart","#postminimalism",
                    "#postmodernart","#postvaporwave","#pointcloud","#psychedelic","#scifi","#spaceart","#spacesofthefuture","#surrealism","#techno","#transdisciplinaryart","#virtualarchive","#virtualart",
                    "#virtualuniverse","#virtualenvironment","#virtualworld","#visualmeditation","#webart"]

hashtags_digital = ["#3Ddesign","#2Dart","#3ddigitalrender","#3dmodel","#3dscan","#aesthetic","#anotherworld","#artistsofinstagram","#AI","#blender","#Bristol",
                    "#Bristolart","#Bristolprogramming","#collage","#computerlearning","#conceptualart","#contemporaryart","#cyberpunk","#cyberart","#cybernetic","#cyborg",
                    "#cyborgsofinstagram","#deepdream","#digitalart","#digitalcollage","#experimentalart","#fineartpractice","#future","#glitchart","#glitchartistscollective",
                    "#graphics","#hyperactivity","#hyperconceptual","#hyperdisciplinaryart","#hyperpractice",
                    "#internet","#internetart","#interdisciplinaryart","#modernart","#minimalart","#minimalismart","#netart","#neuralart","#neuralnetworks","#newcontemporary","#newmedia","#newmediaart",
                    "#opart","#opticalart","#postconceptual","#postinternet","#postinternetart","#postminimalism","#postmodernart","#posthuman","#postvaporwave","#pointcloud","#psychedelic","#scifi","#sculpture",
                    "#surrealism","#techno","#transdisciplinaryart","#virtualarchive","#virtualart","#virtualuniverse","#virtualenvironment","#virtualworld","#visualmeditation","#webart"]
                    
hashtags_physical = ["#2Dart","#3Dart","#3dmodel","#3dscan","#aesthetic","#anotherworld","#artistsofinstagram","#artstudio","#AI","#Bristol","#Bristolart","#collage","#conceptualart",
                     "#contemporaryart","#cyberpunk","#cyberart","#cybernetic","#cyborg","#cyborgsofinstagram","#deepdream","#experimentalart","#fineartpractice","#future","#hyperactivity",
                     "#hyperconceptual","#hyperdisciplinaryart","#hyperpractice",
                     "#internet","#internetart","#interdisciplinaryart","#modernart","#minimalart","#minimalismart","#netart","#neuralart","#neuralnetworks","#newcontemporary","#newmedia","#newmediaart",
                     "#opart","#opticalart","#postconceptual","#postinternet","#postinternetart","#postminimalism","#postmodernart","#posthuman","#postvaporwave","#psychedelic","#scifi","#sculpture","#surrealism",
                     "#technology","#transdisciplinaryart","#virtualart","#visualmeditation","#webart"]
                     
hashtags_phygital = ["#3Dart","#abstract","#2Dart","#3Ddigitalrender","#3Dmodel","#3Dscan","#3Dprinting",
                     "#autonomy","#aesthetic","#anotherworld","#artistsofinstagram","#artstudio","#AI",
                     "#blender","#Bristol","#Bristolart","#Bristolprogramming",
                     "#collection","#collage","#computingart","#conceptualart","#cyberpunk","#critical","#cyberart","#cybernetic","#cyborg",
                     "#cyborgsofinstagram","#deepdream","#digitalart","#digitalcollage","#experimentalart",
                     "#fineartpractice","#future","#glitchart","#glitchartistscollective","#graphics","#hyperactivity",
                     "#hyperconceptual","#hyperdisciplinaryart","#hyperpractice",
                     "#internet","#internetart","#interdisciplinaryart","#modernart","#minimalart","#minimalismart",
                     "#netart","#neuralart","#neuralnetworks","#newcontemporary","#newmedia","#newmediaart",
                     "#opart","#opticalart","#pragmatism","#postconceptual","#postisms","#postinternet","#postinternetart",
                     "#postminimalism","#postmodernart","#postvaporwave","#posthuman","#pointcloud","#psychedelic","#scifi","#sculpture",
                     "#surrealism","#technology","#transdisciplinaryart","#virtual","#virtualarchive","#virtualart",
                     "#virtualuniverse","#virtualenvironment","#virtualworld","#visualmeditation","#webart"]

text_box = tk.Text (root, height = 20, width = 45)

btn_text1 = tk.StringVar()
btn_text2 = tk.StringVar()
btn_text3 = tk.StringVar()
btn_text4 = tk.StringVar()
btn_text5 = tk.StringVar()


btn1 = tk.Button(root, textvariable=btn_text1, command=random_mix_groocks)
btn2 = tk.Button(root, textvariable=btn_text2, command=random_mix_digital)
btn3 = tk.Button(root, textvariable=btn_text3, command=random_mix_physical)
btn4 = tk.Button(root, textvariable=btn_text4, command=random_mix_phygital)
btn5 = tk.Button(root, textvariable = btn_text5, command = copy)

btn_text1.set("Groocks")
btn_text2.set("Digital")
btn_text3.set("Physical")
btn_text4.set("Phygital")
btn_text5.set("Copy")

text_box.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()

root.mainloop()
