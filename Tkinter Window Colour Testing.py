#python 3.7.9
#This program uses the different settings in Tkinter to colour text for the Window GUI in different ways, it's kind like a colour pallet for testing purposes
import tkinter as tk
import random
from random import randint 
data = """'This is line 1.'
'This is line 2.'
'Yet another line.'
'And finally the last line.'
"""
root = tk.Tk()
 
txtwidget = tk.Text(root)
for line in data:
    txtwidget.insert(tk.END, line)
txtwidget.pack(expand=1, fill=tk.BOTH)
 
# adding a tag to a part of text specifying the indices
def highlight_text(tag_name, lineno, start_char, end_char, bg_color=None, fg_color=None):
    txtwidget.tag_add(tag_name, f'{lineno}.{start_char}', f'{lineno}.{end_char}')
    txtwidget.tag_config(tag_name, background=bg_color, foreground=fg_color)
     
highlight_text(tag_name='tag1', lineno=2, start_char=1, end_char=randint(1,20), fg_color='red')
highlight_text(lineno=3, start_char=9, end_char=15, bg_color="black", fg_color='yellow', tag_name='zingo')
 
root.mainloop()
