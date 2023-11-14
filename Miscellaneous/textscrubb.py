# tkinter 
# LR Nov 2023
# Removes the "https://"" from a webaddress - using Tkinter

import os
import tkinter as tk
from tkinter import messagebox, simpledialog,Button, Tk, Label

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def scrubber_window():
    scrubtextbox = simpledialog.askstring("Input", "What is the URL that you want to remove 'https://' from?")
    scrubtextbox = scrubtextbox.strip()
    cleaned = scrubtextbox.removeprefix('https://')
    messagebox.showinfo("Welcome", cleaned)
   
root = tk.Tk()
root.withdraw()
root.destroy()

def main():
    scrubber_window()

if __name__ == '__main__':
    clear_screen()
    main()
