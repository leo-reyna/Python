# LR Nov 2023

import random
import os
os.system("clear")
os.system("cls")

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'Hell no'
    elif answerNumber == 8:
        return 'Outlook ok.'
    elif answerNumber == 9:
        return 'Very Doubtful'
r = random.randint(1,9)
fortune = getAnswer(r)
print (fortune)