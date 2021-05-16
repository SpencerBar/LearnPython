catNames = []
while True:
    print('Enter the name of cat #' + str(len(catNames)+1) + ', or enter nothing to stop:')
    name = input()
    if name == ' ':
        break
    catNames = catNames + [name]
print('The cats names are:')
for name in catNames:
     print(' ' + name)

while True:
    print('Enter a pet name:')
    name = input()

    if name not in catNames:
        print('I do not have a pet named ' + name)
      
    else:
        print(name + ' is my pet.')
    print('Continue?(y/n)')
    temp = input()
    if temp == 'n':
        break