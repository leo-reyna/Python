import random
import os

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

def get_user_question():
    return input("\nAsk a question in your head or say it out loud and once done enter y/n to complete: ")

def display_answer(fortune):
    print(f'\nMagic 8-Ball says: {fortune}')

def get_user_feedback():
    return input("\nDo you want to ask another question? (yes/no): ").lower()

def personalized_greeting():
    user_name = input("What's your name? ")
    print(f"\nHello, {user_name}! Welcome to the Magic 8-Ball.")

def main():
    clear_screen()
    personalized_greeting()

    while True:
        question = get_user_question()

        # Check if the user wants to exit
        if question.lower() == 'exit':
            break

        # Generate a random answer
        answer_number = random.randint(1, 9)
        fortune = get_answer(answer_number)

        # Display the answer
        display_answer(fortune)

        # Ask if the user wants to ask another question
        another_question = get_user_feedback()
        if another_question != 'yes':
            break

if __name__ == "__main__":
    main()
