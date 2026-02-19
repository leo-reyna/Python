import os
os.system("cls")


class Dog: # class name not a function - CLASSES SHOULD ALWAYS BE CAPITALIZED
    def __init__(self, name) -> None: # "name" so you can assign it on Dog ("name of the dog")
        pass
        #self.name = "Rover"
        self.name = name
        self.legs = 4
        self.coat = "furry"

    def speak(self):
        print(self.name + " says bark!")
    def howmanylegs(self):
        print(self.legs)
    def dogcoat(self):
        print(self.coat)
#my_dog = Dog() # instances - they're dog OBJECTS
#another_dog = Dog()

my_dog = Dog("Fluffy")
another_dog = Dog("Rocco")

my_dog.speak()
my_dog.howmanylegs()
another_dog.speak()
another_dog.dogcoat()



