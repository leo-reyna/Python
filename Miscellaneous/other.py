# LReyna - Nov 2023
# From Automate the Boring Stuff with Python book Examples
# While True Examples 

import os
os.system('cls')

while True:
    print('Enter your name: ')
    name = input()
    if name == 'your name':
        break
print('Thank you!!')

# Simple program that asks for a name and password. 
# If the user enters any name besides Joe u, the continue statement v
# causes the program execution to jump back to the start of the loop. When 
# it reevaluates the condition, the execution will always enter the loop, since 
# the condition is simply the value True. Once they make it past that if statement, the user is asked for a password  
# If the password entered is swordfish, then the break statement x is run, and the execution jumps out of the while
# loop to print Access granted y. Otherwise, the execution continues to the end of the while loop, 
# where it then jumps back to the start of the loop. 

while True:
    print('Who are thou? ')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted')


