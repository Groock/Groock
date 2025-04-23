#widgets:
from tkinter import*
from PIL import ImageTk, Image
import random

window = Tk()

#open image

art1 = Image.open('Sim1.PNG')
art2 = Image.open('Sim2.PNG')
art3 = Image.open('Sim3.PNG')
art4 = Image.open('Sim4.PNG')
art5 = Image.open('Sim5.PNG')
art6 = Image.open('Sim6.PNG')

#Resize image1

resized_art1 = art1.resize((400, 250), Image.ANTIALIAS)

new_art1 = ImageTk.PhotoImage(resized_art1)


#Resize image2

resized_art2 = art2.resize((400, 250), Image.ANTIALIAS)

new_art2 = ImageTk.PhotoImage(resized_art2)

#Resize image3

resized_art3 = art3.resize((400, 250), Image.ANTIALIAS)

new_art3 = ImageTk.PhotoImage(resized_art3)

#Resize image4

resized_art4 = art4.resize((400, 250), Image.ANTIALIAS)

new_art4 = ImageTk.PhotoImage(resized_art4)

#Resize image5

resized_art5 = art5.resize((400, 250), Image.ANTIALIAS)

new_art5 = ImageTk.PhotoImage(resized_art5)

#Resize image6

resized_art6 = art6.resize((400, 250), Image.ANTIALIAS)

new_art6 = ImageTk.PhotoImage(resized_art6)

#Image Label

imgLbl = Label( window, image = new_art1 )

#output text box

output= Text(window, width=90, height=8, font=("Helvetica"), wrap=WORD, pady=30, padx=20, background ="white")

#output label and grid postion

output.grid(row=7, column=0, columnspan=6, pady=20)

#Buttons

ABtn = Button( window )
BBtn = Button( window )
CBtn = Button( window )
DBtn = Button( window )
EBtn = Button( window )
FBtn = Button( window )

# Geometry for image label

imgLbl.grid(row = 1, column = 1, rowspan = 6, pady=20 )

#label.grid(row = 3, column = 1, columnspan = 2)

ABtn.grid(row = 1, column = 3)
BBtn.grid(row = 2, column = 3)
CBtn.grid(row = 3, column = 3)
DBtn.grid(row = 4, column = 3)
EBtn.grid(row = 5, column = 3)
FBtn.grid(row = 6, column = 3)

#dynamic properties

def click():
    global imgLbl
    imgLbl.destroy
    imgLbl = Label( window, image = new_art2 )
    imgLbl.grid(row = 1, column = 1, rowspan = 6 )
    output.delete(0.0, END)
    try:       
        Info = random.sample(change,k=1)
        
    except:
        Info = ("Program ERROR")    
    output.insert(END,Info)

def clickB():
    global imgLbl
    imgLbl.destroy
    imgLbl = Label( window, image = new_art3 )
    imgLbl.grid(row = 1, column = 1, rowspan = 6 )
    output.delete(0.0, END)
    try:
        Info = random.sample(doing,k=1)
    except:
        Info = ("Program ERROR")    
    output.insert(END,Info)

def clickC():
    global imgLbl
    imgLbl.destroy
    imgLbl = Label( window, image = new_art4 )
    imgLbl.grid(row = 1, column = 1, rowspan = 6 )
    output.delete(0.0, END)
    try:
        Info = random.sample(reduce,k=1)
    except:
        Info = ("Program ERROR")    
    output.insert(END,Info)

def clickD():
    global imgLbl
    imgLbl.destroy
    imgLbl = Label( window, image = new_art5 )
    imgLbl.grid(row = 1, column = 1, rowspan = 6 )
    output.delete(0.0, END)
    try:
        Info = random.sample(build,k=1)
    except:
        Info = ("Program ERROR")    
    output.insert(END,Info)

def clickE():
    global imgLbl
    imgLbl.destroy
    imgLbl = Label( window, image = new_art6 )
    imgLbl.grid(row = 1, column = 1, rowspan = 6 )
    output.delete(0.0, END)
    try:
        Info = random.sample(being,k=1)
    except:
        Info = ("Program ERROR")    
    output.insert(END,Info)

def clickF():
    global imgLbl
    imgLbl.destroy
    imgLbl = Label( window, image = new_art1 )
    imgLbl.grid(row = 1, column = 1, rowspan = 6 )
    output.delete(0.0, END)
    try:
        Info = random.sample(relax,k=1)
    except:
        Info = ("Program ERROR")    
    output.insert(END,Info)
    
#static properties
window.title('AI Therapy Reminders')
window.resizable(0,0)

ABtn.configure( text = 'Change my thinking patterns',command=click )
BBtn.configure( text = 'Doing things differently',command=clickB )
CBtn.configure( text = 'Reduce my self conciousness',command=clickC )
DBtn.configure( text = 'Build up confidence',command=clickD )
EBtn.configure( text = 'Being more assertive',command=clickE )
FBtn.configure( text = 'Relaxation techniques',command=clickF )

#inital properties
output.configure(state=NORMAL)


    

#lists of strings
change = ['Thoughts affect how you feel, and feelings affect how you think. Changing the way you think will help you to feel better. There are many different kinds of thoughts, many of which most people never have to express in words.' , 'The first step is to identify the ways you think' , 'Some patterns of thinking reflect biases. Biased ways of thinking are unlikely to be right. Many of us have "favourie" biases, and if you know what they are it will be easier to work against them.','The second step is to look for alternative ways of thinking. Good alternatives can usually be expressed in moderate or balanced terms.','Doubting yourself and saying "Yes, but..." makes finding alternatives difficult.','It is easier to find alternatives if you use the kind of compassionate, understanding and encouraging approach that you would adopt if you were helping a freind.','Completing thought records is extremely helpful. Although the exercises can be done in your head, they will be much more effective and much more useful to you in the long run if you also practise doing them on paper.']
doing = ['Doing things differently is one of the most productive ways to build your confidence.','The way to change is to think of yourself as carrying out small experiments, to find out what happens when you change your behavior little by little.','Experiments can help you give up using safety behaviors which otherwise keep the problems going.','Facing things instead of avoiding them also breaks one of the cycles of maintenace, and experimenting with doing this makes it easier to do.','There are many ways in which experiments can help you to change your behavior, and you might be able to think of many different experiments for yourself.','It is less important to worry about whether you will do things wrong, or break a social convention, than to start doing things in the way that you really would like to.','When thinking back on the things that you have done differently it is important not to dismiss or discount your successes. Doing new things may make you more anxious at first, but it will also help to build on your confidence in the long run.']
reduce = ['Self-conscioussness comes from focusing your attention inwards. It is at the centre of all the vicious cycles that help to keep the problem going. It also makes the problem worse.','Focusing attention inwards fills you infomation about yourself and your reactions to feeling anxious. It also means that you have less attention available for things outside yourself. So feeling self-concious leaves you short of accurate, detailed infomation. It leaves you with a hazy impression of what was going on.','Reducing Self-conciousness involves: working out how self-conciouisness affects you; deciding not to think about unpleasant experiences; filling your mind with something else, for example, your five senses.','It is extremely helpful to use your sense of curiosity. Think of yourself as a scientist-explorer who is finding out more about soical interactions. You could carry out two-way experiments, in easy situations first; and you could turn yourself into an accurate, interested and curious observer.','It may take some courage to stop retreating into yourself, and instead to focus on what is happening around you. Although the retreat feels safer, it can make you vulnerable to episodes of self-conciousness. Facing the world is a far safer option in the end.','Self-conciousness influences what you perceive, how you interpret it and what you remember. Broadening your focus of attention changes what you perceive; working on your thoughts can change how you interpret what happens; and doing things in a new way starts to fill your memory with new things, so that the strategies you use fit together well.']
build = ['Confidence is not one thing, but many. It develops from experience, and it comes and goes. Even confident people sometimes feel unconfident.','You can build confidence by behaving "as if" you were confident, and by seeking out successes.','Underlying beliefs and assumptions can undermine confidence. They provide the framework within which you see the world, or the window through which you view it.','Underlying beliefs developed during a lifetime of expereince, and they can be changed.','There are two main steps for changing beliefs: first you need to identify them, so that you know what they are; then you need to re-examine them. To do this you need to step outside the old framework, and search for new infomation.','Building up more positive, helpful beliefs also gives your confidence a surer foundation. So does changing the assumption that go with your beliefs. This involves changing old patterns of behaviour as well as old patterns of thinking.']
being = ['Being interested, but not too curious (or nosy).','Focusing inwards, on your inner experience, as opposed to focusing outwards, only on other people. Talking versus listening','Seeking infomation on the one hand; disclosing infomation on the other.','Talking only about feelings as against talking predominantly about facts.','Recognizing the effects of the past on yourself without being dominated or restricted by it.','Keeping yourself safe at one extreme, and barging in where angels fear to tread on the other.','Revealing intimate things about yourself or clamming up, and saying nothing that might give you away, or give people a hold over you.','Finding the half-way house between being passive and being aggressive.']
relax = ['Progressive muscular relaxation; working through parts of the body in a regular order helps you not to forget any of the muscle groups. Focus your attention on each part of the body, eg clench your fists for a few seconds and release and continue to explore the body.','Adopt a relaxed posture, tension wastes energy, allow your body to relax whenever it can.','Stop rushing about, this is an exhausting habit and quickly wears you out, most people get as much done with a calm relaxed pace.','Plan to do some things that you find relaxing, it does not matter if these things are strenuous or more peaceful, it is the fact that they help you to relax that is helpful.','Seek out things that you enjoy and that give you pleasure, the more you are enjoying yourself, the more relaxed you will feel','Spread the risks, if you put all your eggs in one basket, a treat to the basket will make you tense','Give yourself breaks, short; like reading a magazine, as wells as longer; like a day out or holiday']


#sustain window:
window.mainloop()
