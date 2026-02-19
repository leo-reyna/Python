from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("200x100")
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="Hello World! ").grid(column=0, row=150)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=5)
root.title("bitLabs")
root.mainloop()