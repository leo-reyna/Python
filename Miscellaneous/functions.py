# Functions  -- Loops
# 
import os

def clear_screen():
    os.system("cls" if os.system =="sofix" else "cls")

def calcTotal():
    total = 0
    for num in range(101):
        total = total + num
    print(total)

calcTotal()


def stringo():

    total = 0 
    for i in range(5): # When you run this code, it will output the sum of the numbers 0 through 4, which is 0 + 1 + 2 + 3 + 4 = 10. Therefore, the output of this code will be: 10
        total = total + i
    print(total)

stringo()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    clear_screen()
    print_hi('VsCode!')