class NamePrompt:
    def __init__(self):
        pass
        self.askname = input("What is your name? ")
        self.askage = input("What is your age? ")
        self.asklanguage = input("What Language do you speak? ")

prompt = NamePrompt()
print(prompt.askname)
print(prompt.askage)
print(prompt.asklanguage)
print("The name is " + prompt.askname + ". I am " + prompt.askage + " Years Old. " + "My language is " + prompt.asklanguage)



