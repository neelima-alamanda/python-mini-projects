# Initialize an empty list to store all recipes
recipes = []

def add_recipe():
    """
    Function to add a new recipe to the recipes list.
    Prompts the user for recipe details such as name, ingredients, category, and calories.
    """
    # Input for recipe name with validation
    while True:
        recipe_name = input("Enter Recipe Name: ").strip()
        if recipe_name:  # Ensure the recipe name is not empty
            break
        else:
            print("Recipe name cannot be empty.")
    
    # Input for the number of ingredients with validation
    while True:
        try:
            ingredients_count = int(input("Enter number of ingredients: "))
            if ingredients_count > 0:  # Number must be greater than zero
                break
            else:
                print("Number of ingredients must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")  # Handle invalid input
    
    # Collect the ingredients one by one
    ingredients = []
    for i in range(ingredients_count):
        while True:
            ingredient = input(f"Enter Ingredient {i+1}: ").strip()
            if ingredient:  # Ingredient cannot be empty
                ingredients.append(ingredient)
                break
            else:
                print("Ingredient cannot be empty.")
    
    # Input for meal type with validation
    while True:
        meal_type = input("Enter Meal Type (Breakfast/Lunch/Dinner): ").title()
        if meal_type in ("Breakfast", "Lunch", "Dinner"):  # Must match one of these options
            break
        else:
            print("Please enter Breakfast, Lunch or Dinner.")
    
    # Input for food type with validation
    while True:
        food_type = input("Enter Food Type (Vegetarian/Non-Vegetarian): ").title()
        if food_type in ("Vegetarian", "Non-Vegetarian"):  # Must match one of these options
            break
        else:
            print("Please enter Vegetarian or Non-Vegetarian.")
    
    # Combine meal type and food type into a tuple for category
    category = (meal_type, food_type)
    
    # Input for estimated calories with validation
    while True:
        try:
            calories = int(input("Enter Estimated Calories: "))
            if calories > 0:  # Calories must be greater than zero
                break
            else:
                print("Calories must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")  # Handle invalid input
    
    # Create a dictionary for the recipe and add it to the `recipes` list
    recipe = {
        "name": recipe_name,
        "ingredients": ingredients,
        "category": category,
        "calories": calories,
    }
    recipes.append(recipe)  # Append the recipe to the list
    print("Recipe added successfully!")  # Confirmation message

def view_recipes():
    """
    Function to display all the recipes in the recipes list.
    If no recipes are available, it notifies the user.
    """
    if not recipes:  # Check if the recipes list is empty
        print("No Recipes Available")
        return

    # Iterate through each recipe and display its details
    for recipe in recipes:
        print("Recipe Name:", recipe["name"])
        print("Ingredients:")
        for item in recipe["ingredients"]:
            print("-", item)  # Display each ingredient
        print()
        print("Meal Type :", recipe["category"][0])  # First item in the category tuple
        print("Food Type :", recipe["category"][1])  # Second item in the category tuple
        print("Calories:", recipe["calories"])
        print("-" * 40)  # Separator line between recipes

def search_recipe_by_ingredient():
    """
    Function to search for recipes by a specific ingredient.
    Prompts the user to enter an ingredient and displays recipes that contain it.
    """
    search_item = input("Enter ingredient to search: ").lower()  # Normalize the input for case-insensitive matching
    if not recipes:  # Check if the recipes list is empty
        print("No recipes available")
        return
    
    found = False  # Flag to track if a matching recipe is found
    for recipe in recipes:
        for ingredient in recipe["ingredients"]:  # Search through each recipe's ingredients
            if search_item == ingredient.lower():  # Case-insensitive comparison
                print("\nRecipe Found!")
                print(f"Recipe Name : {recipe['name']}")
                print(f"Meal Type   : {recipe['category'][0]}")
                print(f"Food Type   : {recipe['category'][1]}")
                print(f"Calories    : {recipe['calories']}")
                found = True
                break  # Stop searching this recipe if the ingredient is found
    if not found:  # If no recipe was found, display a message
        print("Recipe not Found")

def analyze_nutrition():
    """
    Function to analyze and display nutritional information about the recipes.
    Calculates total recipes, average calories, and the count of vegetarian/non-vegetarian recipes.
    Also identifies unique ingredients and displays high-calorie recipes (calories > 500).
    """
    if not recipes:  # Check if the recipes list is empty
        print("No Recipes available")
        return
    
    # Initialize variables for analysis
    total_recipes = len(recipes)
    total_calories = 0
    vegetarian = 0
    non_vegetarian = 0
    unique_ingredients = set()
    high_found = False  # Flag to track if high-calorie recipes exist

    # Iterate through each recipe to calculate nutritional stats
    for recipe in recipes:
        total_calories += recipe["calories"]  # Sum of all calories
        if recipe["calories"] > 500:  # Check for high-calorie recipes
            if not high_found:  # Print heading only once
                print("\nHigh Calorie Recipes:")
                high_found = True
            print("Recipe Name:", recipe["name"])
            print("Calories:", recipe["calories"])
        # Count recipes by food type
        if recipe["category"][1] == "Vegetarian":
            vegetarian += 1
        else:
            non_vegetarian += 1
        # Add unique ingredients to the set
        unique_ingredients.update(recipe["ingredients"])
    
    if not high_found:
        print("\nNo High Calorie Recipes Found.")  # If no high-calorie recipes were found

    # Calculate the average calories
    average = total_calories / total_recipes

    # Display the results of the analysis
    print("\nNutrition Analysis")
    print("-" * 40)
    print("Total Recipes:", total_recipes)
    print(f"Average Calories: {average:.2f}")
    print("Vegetarian Recipes:", vegetarian)
    print("Non-Vegetarian Recipes:", non_vegetarian)
    print("\nUnique Ingredients:")
    for item in unique_ingredients:
        print(item)
    print("\nHealthy cooking starts with healthy choices! 🥗")

def main():
    """
    Main function that provides the menu interface to perform operations.
    Users can add recipes, view recipes, search recipes, and analyze nutrition.
    """
    print("=" * 40)
    print("🍽️ RECIPE ORGANIZER 🍽️")
    print("Organize your favorite recipes with ease!")
    print("=" * 40)
    while True:
        # Display the main menu
        print("\n========== MENU ==========")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Search Recipe")
        print("4. Analyze Nutrition")
        print("5. Exit")
        print("=" * 25)
        
        # Validate the user's menu choice
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= 5:
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Perform the action based on the user's choice
        if choice == 1:
            add_recipe()
        elif choice == 2:
            view_recipes()
        elif choice == 3:
            search_recipe_by_ingredient()
        elif choice == 4:
            analyze_nutrition()
        elif choice == 5:
            print("\nThank you for using Recipe Organizer!")
            break
        else:
            print("Invalid choice.")

# Entry point of the program
if __name__ == "__main__":
    main()