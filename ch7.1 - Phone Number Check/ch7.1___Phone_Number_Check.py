
""" 
def findPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range (4, 7):
            if not text[i]. isdecimal():
                return False
        if text[7] != '-':
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if findPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
"""
import re
def findPhoneNum(text):

    # phoneNumRegex = re.compile(r'(\d{3})?-(\d{3}-\d{4})')
    phoneNumRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?           # area code
        (\s|-|\.)?                   # separator
        \d{3}                        # first 3 digits
        (\s|-|\.)                    # separator
        \d{4}                        # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})? # extension
        )''', re.VERBOSE)
    mo = phoneNumRegex.findall(text)
    for i in range(len(mo)):
       print('Phone number found: ' + str(mo[i]))
    return mo

text = ('My number is 415-555-4242.')
findPhoneNum(text)

text1 = ('Cell: 415-555-9999 Work: 212-555-0000')
x = findPhoneNum(text1)
print(x)

def inventorySearch(itemlist):
    itemRegex = re.compile(r'\d+\s\w+')
    loot = itemRegex.findall(itemlist)
    print("You've looted:" + str(loot))
    return loot

loot = ('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, \
7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
inventorySearch(loot)
