#python 3.7.9

#This program is for an A.I bot that you can speak to and it speaks back to you.
#This program was made for a bot art installation for my Masters degree. The bot uses recordigs via microphone and converts them to text, sends them to an A.I API (which may no longer work, haven't tested) and then get responces which it then turns into A.I voice and plays it through speakers. Basically creating a janky A.I bot that you can speak to you and it speaks back to you.

#talking subject program by George Thom
from gtts import gTTS
import os
import playsound
import openai
from chronological import main, read_prompt, gather, cleaned_completion
from time import *
import threading

# Load your API key from an environment variable or secret management service
openai.api_key = ("redacted")#os.getenv("OPENAI_API_KEY")
text1 = None
on = True
progress = 0
result = None
user_text_available = threading.Event()
result_available = threading.Event()

#buffer size
bufsize=250
#size of text bytes in dragon pad
sizeofinput=0

def gettext():
     import pywin32 as win32gui
     import win32con
     global text1
     global result_available

     #initalize variables
     buf = None

     length = None

     #find the dragon pad window
     window = win32gui.FindWindow(('TalkpadClass'),None)
     
     title = win32gui.GetWindowText(window)

     control = win32gui.FindWindowEx(window, 0, 'RICHEDIT50W', None)

     #get size of the text in dragon pad
     sizeofinput=win32gui.SendMessage(control, win32con.WM_GETTEXTLENGTH)
     print ('size of input: '+str(sizeofinput))

     #make buffer size match the input
     bufsize=sizeofinput*2
     print ('size of bufsize: '+str(bufsize))
     
     #make buffer for the bytes
     buf = win32gui.PyMakeBuffer(bufsize)

     #send message to dragon pad to send text back as bytes
     length = win32gui.SendMessage(control, win32con.WM_GETTEXT, bufsize, buf)

     result = buf[0:length*2]

     #decode the bytes to string in utf16
     text1 = (result.tobytes().decode("utf-16"))

     #strip the string of usless characters
     text1 = (text1.replace('.',''))

     if text1 == (" ") or ("") or None:
          print('Gettext: There is no text from user')
          sleep(1)
          result_available.clear()
          gettext()

     #text is present in text1
     else:

          print ('Got the text at gettext finish, result_available flag set. ')
          print ('Gettext from user is: '+text1)
          result_available.set()
          sendtoai()

def deletetext():

     import win32gui
     import win32con

     window = win32gui.FindWindow(('TalkpadClass'),None)
     title = win32gui.GetWindowText(window)

     control = win32gui.FindWindowEx(window, 0, 'RICHEDIT50W', None)
     buf = (' ')
     length = win32gui.SendMessage(control, win32con.WM_SETTEXT, 300, buf)

     result = buf[0:length*2]
     
     print ('Deletetext deleted text in dragon')

     if text1 == (" ") or ("") or None:
          print ('No text and delete text completed sending to get text')
          gettext()
          
     else:
          print ('Delete text completed and sending to ai')
          speak()

def speak():
     from playsound import playsound
     global text1
     global prompt
     global tts
     import os
     import pyglet
     
     tts = gTTS(text=text1+formedtext, lang='en')
     
     filename = ("new.mp3")
     print (filename)
     tts.save(filename)
     music = pyglet.media.load(filename, streaming=False)
     music.play()
     sleep(music.duration) #prevent from killing
     try:
          os.remove(filename)#remove temperory file
          print('Mp3 file removed')
     except:
          print ('No file')
     prompt = None
     text1 = None
     print ('Speak finished')
     #gettext()
     

async def logic():
     print('async logic start')
     # you call the Chronology functions, awaiting the ones that are marked await
     global prompt
     global text1
     global formedtext

     if text1 == (" ") or ("") or None:
          prompt = ("");
          print (prompt)
          print ('Text at logic blank: '+text1)
          sleep(1)
          logic()
     else:
          prompt = (text1)
          print (prompt)
          print ('Text at logic else: '+text1)
     completion = await cleaned_completion(prompt, max_tokens=20, engine="davinci",
                                          temperature=0.8, top_p=1, frequency_penalty=0.2, stop=["none"])

     formedtext=('{0}'.format(completion))
     print(formedtext)
     formedtext = (formedtext.replace('.', ' ').replace('-',' ').replace('~',' ').replace('_',' '))
     print('Stripped text: '+formedtext)
     deletetext()
    
def sendtoai():
     print('sendtoai start')
     global main
     main(logic)

def main2():
     global result_available

     print('Main2 starting thread gettext')
     thread = threading.Thread(target=gettext)
     thread.start()

     print('Main2 initialize')

     # wait here for the result to be available before continuing
     #while result_available.wait(timeout=5):
         #print('\r{}% done...'.format(progress), end='', flush=True)
     print('\r{}% done...'.format(progress))

     print('Main2 fin starting delete text')
     threading.enumerate()
     deletetext()

while on == (True):
          gettext()
     
