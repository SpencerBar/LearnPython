#! python3
#a program to check if a password is strong
import re
def passwordStrength(password):

    passStr = 0
#Check for 8 character length
    if len(password) >= 8:
        passStr += 1
        #print('password length: ' + str(len(password)))
        #print(passStr)
#Check for capital letters
    capLetters = re.compile(r'[A-Z]')
    if (capLetters.search(password) != None):
       passStr += 1
    #print((capLetters.search(password)))
    #print(passStr)

#Check for lowercase letters
    lowLetters = re.compile(r'[a-z]')
    if(lowLetters.search(password) != None):
        passStr += 1
    #print(lowLetters.search(password))
    #print(passStr)
    
#Check for symbols
    symbolRegex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(symbolRegex.search(password) != None):
        passStr += 1
    #print(symbolRegex.search(password))
    #print(passStr)
#Determine strength of password
    if passStr == 0:
        print("Your password is Pathetic!")
    if passStr == 1:
        print("your password is Weak!")
    if passStr == 2:
        print("Your password is Mediocre!")
    if passStr == 3:
        print("Your password is Strong!")
    if passStr == 4:
        print('Thanos is that you? Your password is Very Strong!')


text = 'wdEfwT%dgAr'
passwordStrength(text)