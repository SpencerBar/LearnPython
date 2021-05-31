#! python3
#bullet point adder, adds bullet points to the start
#of each line in a list

import pyperclip

text = pyperclip.paste()#copy list from clipboard

lines = text.split('\n')#seperate lines

for i in range(len(lines)): #loop through all indexes in lines 
    lines[i] = '*' + lines[i]  #add stars

pyperclip.copy(text)


