# LR


import os

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


def display_name():
    first_name = "ada"
    last_name = "lovelace"
    full_name =f'{first_name} {last_name}'
    print(full_name.title())
    textscrub = input('Enter the url: ')
    cleaned = textscrub.removeprefix('https://')
    print(cleaned)
    

if __name__ == '__main__':
    clear_screen()
    display_name()