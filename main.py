# Завдання 2
# Створіть клас Cart
# Атрибути:
#  user – ім’я користувача
#  items – список товарів
#  total – загальна ціна
# Методи:
#  add(item, price) – добавити товар у кошик
#  delete(item, price) – видалити товар з кошика
#  info() – вивести інформацію про кошик
# save(fiename) – зберегти дані у файл(за замовчуванням cart.json)
#  load(fiename) – завантажити дані з файла(за замовчуванням cart.json)

import json


class Cart:
    def __init__(self, user):
        self.user = user
        self.items = []
        self.total = 0

    def add(self):
        item = input("Введіть товар: ")
        price = float(input("Та вкажіть його ціну: "))

        self.items.append(item)
        self.total += price

    def delete(self, item, price):
        if item in self.items:
            self.items.remove(item)
            self.total -= price
        else:
            print(f"Товару \"{item}\" немає в кошику.")

    def info(self):
        print()
        print(f"У кошику клієнта {self.user} знаходяться такі товари:")
        for item in self.items:
            print(f"\t{item}")
        print(f"На загальну суму: {self.total:.2f} грн.")

    # save(fiename) – зберегти дані у файл(за замовчуванням cart.json)
    def save(self, filename="cart.json"):
        with open(filename, 'r', encoding='utf-8') as file:
            data_all = json.load(file)

        data_all[self.user] = {
            "items": self.items,
            "total": self.total,
        }

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data_all, file, indent=4)

    #  load(fiename) – завантажити дані з файла(за замовчуванням cart.json)
    def load(self, filename="cart.json"):
        with open(filename, 'r', encoding='utf-8') as file:
            data_dict: dict = json.load(file)
        user_data = data_dict[self.user]
        print(user_data)
        self.items = user_data["items"]
        self.total = user_data["total"]



if __name__ == '__main__':
   my_cart = Cart("John")

   my_cart.add()
   my_cart.add()
   my_cart.info()

   my_cart.save()

   my_cart1 = Cart("Mary")
   my_cart1.add()
   my_cart1.save()
   my_cart1.info()
