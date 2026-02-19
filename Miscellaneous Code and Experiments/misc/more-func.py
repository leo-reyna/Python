import os
os.system("cls")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + str(self.name) + " and I am " + str(self.age))

p1 = Person("John", 36)
p1.myfunc()


class Whatup: #defining the class 
   def __init__(self, greeting, name, age):
    self.greeting = greeting
    self.age = age
    self.name = name
    
   def sayhi(self):
    print("Hey " + str(self.greeting) + str(self.name) + str(self.age))
   
customer = Whatup("Wassup ", "Leo", " you are 44")
customer.sayhi()
texto = "we are the so-called \"Vikings\" from the north." 

# string methods
print(texto.capitalize())
print(texto.upper())