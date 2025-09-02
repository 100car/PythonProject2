# Завдання 1
# Створіть клас Recipe з атрибутами
#    name – назва страви
#    ingredients – список продуктів
#    text – текст рецепту
#    time – час приготування
# методи:
#    __str__(self) – повертає назву страви
#    __contains__(self, item) – перевіряє чи є інгредієнт в рецепті
#    __gt__(self, other) – перевіряє чи є час приготування self більшим за other
#    display_info(self) – виводить всю інформацію про рецепт
# Створіть декілька рецептів та добавте їх у список.
# Виведіть назви тих рецептів, які містять інгредієнт томат
# Виведіть повну інформацію рецепта з найменшим часом приготування, скористайтесь функцією min

class Recipe:
    def __init__(self, name, ingredients, text, time):
        self.name = name
        self.ingredients = ingredients or []
        self.text = text
        self.time = time

    def __str__(self):
        return f"{self.name}"

    def __contains__(self, item):
        return item.lower() in (ing.lower() for ing in self.ingredients)

    def __gt__(self, other):
        return self.time > other.time
        # if self.time > other:
        #     print(f"Час {self.time} більший, ніж {other}")
        # else:
        #     print(f"Час {self.time} менший, ніж {other}")

    def display_info(self):
        print(f"Рецепт '{self.name}':")
        print(f"\tСписок продуктів: {', '.join(self.ingredients)}.")
        print(f"\tРецепт: {self.text}.")
        print(f"\tЧас приготування: {self.time} хв.")

recipe1 = Recipe("Піца",
 ["борошно", "вода", "дріжджі", "томат", "сир"],
 "Готуємо тісто, додаємо інгредієнти та запікаємо", 30)

recipe2 =Recipe("Салат",
 ["томат", "огірок", "зелень", "олія"],
 "Нарізаємо овочі, додаємо зелень та поливаємо олією", 10)

recipe3 = Recipe("Суп",
 ["вода", "картопля", "морква", "м'ясо"],
 "Варимо всі інгредієнти до готовності",45)

recipe_list = [recipe1, recipe2, recipe3]
# тестуємо
# for _ in recipe_list:
#     _.display_info()

# Виведіть назви тих рецептів, які містять інгредієнт томат
print("Інгредієнт 'томат' є в таких рецептах:")
for item in recipe_list:
    if "томат" in item:
        print(item)

# Виведіть повну інформацію рецепта з найменшим часом приготування
print("\nРецепт з найменшим часом приготування:")
min_recipe = min(recipe_list)
min_recipe.display_info()







