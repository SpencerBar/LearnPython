def Collatz(number):
    print(number)
    while True:
        if (number % 2== 0):
            number = int(number/2)
            print(number)
        elif number == 1:
           break
        else:
            number = int((number * 3)+1)
            print(number)




while True:
    try:
        print('Enter an number:', end=' ')
        NumIn = int(input())
    except ValueError:
        print('Sorry, invalid input.')
    else:
        break
Collatz(NumIn)