# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами client(ім’я клієнта)
# та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик

# class Cart:
#     def __init__(self, client, items = None):
#         if items is None:
#             items = []
#         self.client = client
#         self.items = items
#
#     def add_item(self, item_plus):
#         self.items.append(item_plus)
#         print(f"Клієнт магазину {self.client} додав до свого кошика {item_plus}.")
#
#     def remove_item(self, item_minus):
#         if item_minus in self.items:
#             self.items.remove(item_minus)
#             print(f"Клієнт магазину {self.client} видалив зі свого кошика {item_minus}.")
#         else:
#             print(f"В кошику клієнта {self.client} немає {item_minus}. Видалення неможливе.")
#
#     def print_info(self):
#         print(f"У клієнта {self.client} в кошику такий набір продуктів:")
#         print(", ".join(self.items))
#
# cart1 = Cart("Шевченко")
#
# cart1.add_item("буряк")
# cart1.add_item("молоко")
# cart1.add_item("буряк")
# cart1.add_item("огірки")
# cart1.add_item("буряк")
#
# cart1.remove_item("ананас")
# cart1.remove_item("буряк")
#
# cart1.print_info()

# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level. Додайте метод,
# який зменшує заряд телефона(на скільки зменшити відсотків передається як параметр),
# якщо він опуститься нижче 20%, вивести повідомлення.
# Додайте метод для виведення інформації про телефон.

class Phone:
    def __init__(self, number, battery_level = 100):
        self.number = number
        self.battery_level = battery_level
        if self.battery_level < 0:
            self.battery_level = 0
        if self.battery_level > 100:
            self.battery_level = 100

    def drain_battery(self, percents):
        self.battery_level = max(self.battery_level - percents, 0)
        if self.battery_level < 20:
            print(f"Заряд телефону {self.battery_level}%!")

    def print_info(self):
        print(f"Телефон з номером {self.number} має заряд {self.battery_level}%.")

my_number = Phone("+380673828282", battery_level=90)
my_number.print_info()
my_number.drain_battery(20)
my_number.print_info()
my_number.drain_battery(60)
my_number.drain_battery(30)



