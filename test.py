from models import Recipe


# file = Recipe.File.import_file()


data = {'recipe_name': 'Pan Cake', 'instruction': '1. Cook the spaghetti according to package instructions.\n2. In a pan, cook the guanciale or pancetta until crispy.\n3. In a separate bowl, mix eggs, pecorino cheese, salt, and black pepper.\n4. Drain cooked spaghetti and mix with the egg-cheese mixture.\n5. Add spinach.\n6. Serve hot, garnished with minced garlic and chopped parsley.', 'preparation_time_minutes': "20", 'cooking_time_minutes': "15", 'servings': "4", 'calories': "69", 'category': 'pasta'}
# Recipe.Recipe.add(data)
# Recipe.Recipe.delete(3)
Recipe.Recipe.update(1,data)