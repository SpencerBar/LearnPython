tableData=[['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    maxChar = 0 # max characters in list starts at zero
    for i in range(len(table)):#iterate through words in the table
        for word in table[i]:
            if maxChar < len(word): # determine the max character length of all the words
                maxChar = len(word) # and assign it to maxChar
    for i in range(len(table[0])):
        for word in range(len(table)):
           print(table[word][i].rjust(maxChar),end = ' ') # print the woirds with additional spaces accoridng to maxChar
        print() # for newline
        i +=1
printTable(tableData)