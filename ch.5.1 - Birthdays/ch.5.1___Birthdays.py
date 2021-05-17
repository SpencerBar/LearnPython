birthdays = {'Alice': '04/01/1992','Bob': '12/12/1957 ', 'Carol': '03/04/1999'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?(MM/DD/YYYY)')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
