#python 3.7.9

#Artist statment generator, I used my Masters thesis for the input text file, but other files can be inputed into text file in same folder as this program with name myFile.txt 

# import required module 
import random
import time
import linecache
import textwrap

loop = 1  
# print random word
while loop < 100 :
    a=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    b=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    c=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    d=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    e=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    f=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    g=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    h=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    i=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))
    j=(random.choice(open("myFile.txt","r",encoding='utf8').read().split()))


    #aa=("How do we use science fiction and the ")+a+(" to be more speculative about the ")+b+("?")#+c+(" ")+d+(" ")+e+(" ")+f+(" ")+g+(" ")+h+(" ")+i+(" ")+j+(" ")+k+(" ")+l+(" ")+m+(" ")+n+(" ")+o+(" ")+p+(" ")+q+(" ")+r+(" ")+s+(" ")+t
    aa=textwrap.fill((" As a digital curator and contemporary artist focusing on ")+a+
    (", George Thom intends to make visible the ")+b+
    (" and ")+c+
    (". The role of the image in determining ")+d+
    (" has a long history, technologies of ")+e+
    (" have shaped ")+f+(". George seeks to address questions of ")+g+(", ")+h+(" and ")+i+(". Using the method of ")+j,width=70)#+(" ")+k+(" ")+l+(" ")+m+(" ")+n+(" ")+o+(" ")+p+(" ")+q+(" ")+r+(" ")+s+(" ")+t


    print (aa+"\n")
    time.sleep(7)
    
