class RecipeBook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, name, ingredients, instructions):
        self.recipes[name] = {
            'ingredients': ingredients,
            'instructions': instructions
        }

    def search_recipe(self, keyword):
        found_recipes = []
        for name, recipe in self.recipes.items():
            if keyword.lower() in name.lower():
                found_recipes.append(name)
        return found_recipes

    def display_recipe(self, name):
        if name in self.recipes:
            recipe = self.recipes[name]
            print(f"Recipe: {name}")
            print("Ingredients:")
            for ingredient in recipe['ingredients']:
                print(f"  - {ingredient}")
            print("Instructions:")
            for idx, step in enumerate(recipe['instructions'], start=1):
                print(f"  {idx}. {step}")
        else:
            print(f"Recipe '{name}' not found.")

def main():
    recipe_book = RecipeBook()

    while True:
        print("\nRecipe Book Menu:")
        print("1. Add Recipe")
        print("2. Search Recipe")
        print("3. Display Recipe")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            instructions = input("Enter instructions (one per line, type 'done' to finish):\n")
            instructions = []
            while True:
                step = input()
                if step.lower() == 'done':
                    break
                instructions.append(step)
            recipe_book.add_recipe(name, ingredients, instructions)
            print(f"Recipe '{name}' added successfully.")

        elif choice == '2':
            keyword = input("Enter keyword to search: ")
            found_recipes = recipe_book.search_recipe(keyword)
            if found_recipes:
                print("Found recipes:")
                for recipe in found_recipes:
                    print(f"  - {recipe}")
            else:
                print("No recipes found.")

        elif choice == '3':
            name = input("Enter recipe name: ")
            recipe_book.display_recipe(name)

        elif choice == '4':
            print("Exiting Recipe Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
