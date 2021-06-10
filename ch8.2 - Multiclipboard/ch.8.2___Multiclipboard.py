#! python3
# multiclipboard.pyw - saves and loads pieces of text to the clipboard.
# usage: py.exe Mutliclipboard.pyw save <keyword> - Saves clipboard to keyword
#        py.exe Mutliclipboard.pyw <keyword> - loads keyword to clipboard
#        py.exe Mutliclipboard.pyw list - loads all keywords into clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #todo list keywords and load contet
    if sys.argv[1].lower == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close() 