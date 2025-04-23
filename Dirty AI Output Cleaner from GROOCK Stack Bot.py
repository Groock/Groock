#this is specific use program that searches dirty A.I responces that were generated from a complex A.I voice recgnoition speaking bot called GROOCKS that existed in an art gallery at Bath Spa for my Master degree. The A.I responces are text files and the program extracts responces and the prompts that were sent to the A.I via voice recording.

#change the name of the file to clean
dirtyfile=('ways to save the world')

file = open((dirtyfile+'.txt'), encoding="utf8")
filenew = open('Computer_Cleaned_Ideas_003.txt', 'w', encoding="utf16")

print('File Name:' , file.name)
print('File Open Mode:' , file.mode)
print(' Readable:' , file.readable())
print('Writeable:' , file.writable())

for line in file:
     if "Prompt:" in line:
          print (line, end = '')
     if '"text":' in line:
          print (line, end = '')
          
file.close()
