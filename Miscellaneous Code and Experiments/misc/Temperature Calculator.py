# this is my first program
import os
import sys
os.system('cls')


print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
print("▓▓▓▓▓ TEMPERATURE CONVERTER ▓▓▓▓▓")
print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
print("      Fahrenheit to Celsius")
print("      =====================")
print("What is the temperature: ")
myFahrenheit = input()
treinta = 32
Cel = ((int(myFahrenheit) - treinta) * 5) // 9
print("The Temperature is: " + (str(Cel) + chr(176) +" Celsius"))


# print("hello world!")
# print("What is your name ")
# myName = input()
# print('it is good to meet you ' + myName)
# print("the length of your name is ")
# print(len(myName))
