# LR 2023
# String Exercises


firstName ='ada'
lastName = 'lovelace'
fullName = f"{firstName} {lastName}"
print(fullName.title()) # Proper Name
print(fullName[0].title()) # Capitalize the first value


bicycles = ['jules', 'trek', 'cannonball', 'redline']
message = f"My First bicycle was a {bicycles[0].title()}."
print(bicycles[1]) # 2nd Item in the list = Trek
print(bicycles[2]) # 3rd item in the list = Cannonball
print(bicycles[-1]) # last item in the list
print(message)

# Modifying, Adding, and Removing  Elements

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati' #adding ducati to first pos removing Honda
print(motorcycles)
