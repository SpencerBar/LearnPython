import random

rannum = random.randint(1, 20)
print('Guess the number between 1 and 20,')
for i in range(1, 7):
   print('Take a guess')
   guess = int(input())
   if guess < rannum:
       print('Your guess was too low!')
       print('You have guessed ' + str(i) + '/6 times')
   elif guess > rannum:
       print('Your guess was too high!')
       print('You have guessed ' + str(i) + '/6 times')
   else:
      break


if guess == rannum:
    print("You've guessed right!")
else:
   print('You tried your best, but the number was ' + str(rannum))