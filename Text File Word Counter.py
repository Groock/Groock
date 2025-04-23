#python 3.7.9
#this program counts individual words in a file and output a table in the python shell E.G OrderedDict([('the', 4071), ('of', 2411), ('a', 1903), ('to', 1688). With the word and the amount of times it appears in the text, for this I was counting the usage of words in the text Actor-Network Theory.

from collections import OrderedDict

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return OrderedDict(sorted(counts.items(), key=lambda t: t[1], reverse=True))

file = open('Text.txt', 'r', encoding='UTF-8' )

lines = file.readlines()

filestring=""

for i in lines:
   filestring=filestring+i+""

filestring = filestring.lower()

filestring = filestring.replace('.',' ').replace(',',' ').replace("’",' ')
filestring = filestring.replace("‘",' ').replace("“",' ').replace("”",' ')
filestring = filestring.replace("!",' ').replace("(",' ').replace(")",' ')
filestring = filestring.replace("?",' ').replace("{",' ').replace("}",' ')
filestring = filestring.replace("~",' ').replace("[",' ').replace("]",' ')
filestring = filestring.replace("/",' ').replace(";",' ').replace(":",' ')
filestring = filestring.replace('…',' ').replace(";",' ').replace(":",' ')

print( word_count(filestring))
