#!
# Password Protector
PASSWORDS = {'Email': 'FweB34Bsdf7jw95e3fjQ2',
            'Instagram': 'sJH33vH58VK43v6Kuv',
            'Warframe': 'y4jL6Kw9ertJ34bv',} 

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy  account password')
    sys.exit()

account = sys.argv[1] # the first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for {account} copied to clipboard') # f' ' to include variuables without +
else:
    print(f'There is no account named {account} in the file')