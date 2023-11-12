# tkinter 
# LR 2023

import os
import tkinter as tk
from tkinter import messagebox, simpledialog,Button, Tk, Label

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def scrubber_window():
    scrubtextbox = simpledialog.askstring("Input", "What is the URL?")
    scrubtextbox = scrubtextbox.strip()
    cleaned = scrubtextbox.removeprefix('https://')
    messagebox.showinfo("Welcome", cleaned)


root = tk.Tk()
root.withdraw()

def main():
    scrubber_window()


if __name__ == '__main__':
    clear_screen()
    main()
