import random

#def GetAnswer(AnswerNumber):
 #   if AnswerNumber == 1:
  #      return 'It is certain'
  #  elif AnswerNumber == 2:
  #      return 'It is decidedly so'
  #  elif AnswerNumber == 3:
  #      return 'Yes'
  #  elif AnswerNumber == 4:
  #      return 'Reply hazy, try again'
 #   elif AnswerNumber == 5:
 #       return 'Ask again later'
 #   elif AnswerNumber == 6:
 #       return 'Concentrate and ask again later'
 #   elif AnswerNumber == 7:
 #       return 'My reply is no'
 #   elif AnswerNumber == 8:
 #       return 'Outlook is not good'
 #   elif AnswerNumber == 9:
 #       return 'Very Doubtful'
 #   elif AnswerNumber == 10:
 #       return 'No'
#print(getAnswer(random.randint(1, 9)))


messages = ['It is certain',
 'It is decidedly so',
 'Yes definitely',
 'Reply hazy try again',
 'Ask again later',
 'Concentrate and ask again',
 'My reply is no',
 'Outlook not so good',
 'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])
