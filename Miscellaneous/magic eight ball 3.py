import random
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def get_answer(answer_number):
    answers = {
        1: 'It is certain',
        2: 'It is decidedly so',
        3: 'Yes',
        4: 'Reply hazy, try again',
        5: 'Ask again later',
        6: 'Concentrate and ask again',
        7: 'Hell no',
        8: 'Outlook ok.',
        9: 'Very Doubtful'
    }
    return answers.get(answer_number, 'Invalid answer number')

def generate_answer():
    answer_number = random.randint(1, 9)
    return get_answer(answer_number)

def display_answer():
    fortune = generate_answer()
    messagebox.showinfo("Magic 8-Ball", f'Magic 8-Ball says: {fortune}')

def exit_app():
    root.destroy()

def personalized_greeting():
    user_name = simpledialog.askstring("Input", "What's your name?")
    user_name = user_name.strip() # remove whitespaces from both ends
    messagebox.showinfo("Welcome", f"Hello, {user_name}! Welcome to the Magic 8-Ball.")

# Create the main window
root = tk.Tk()
root.title("Magic 8-Ball")

# Create a label for instructions
label = tk.Label(root, text="Ask a question and click 'Get Answer'")
label.pack(pady=10)

# Create a button to get an answer
button = tk.Button(root, text="Get Answer", command=display_answer)
button.pack(pady=20)

# Create a button to exit the application
exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5)

# Run the personalized greeting on startup
personalized_greeting()

# Run the Tkinter event loop
root.mainloop()
