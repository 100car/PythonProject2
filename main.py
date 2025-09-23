# Завдання 1
# Використовуючи бінарні дерева, організуйте роботу автопарку, де зберігаються автомобілі, відсортовані за моделлю(!)
# У однієї марки може бути багато моделей. У кожної моделі її марки унікальні.
# Клас Car
# Атрибути:
#  brand – марка (бренд, виробник) автомобіля
#  model – модель автомобіля
#  year – рік випуску

import bintrees


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand:<15}{self.model:<10}\t{self.year}"


class CarPark:
    def __init__(self):
        self.cars = bintrees.AVLTree()

    def add(self, brand, model, year):
        """Додати автомобіль у автопарк"""
        car = Car(brand, model, year)
        self.cars.insert(key=model, value=car)

    def display(self):
        """Вивести всі авто"""
        print()
        for model in self.cars:
            print(self.cars[model])

    def remove(self, model):
        """Видалити автомобіль"""
        self.cars.remove(model)

    def search(self, model):
        """Пошук авто за моделлю"""
        return self.cars.get(model, None)

    def __len__(self):
        """Кількість авто"""
        return len(self.cars)

    def sell_car(self, client, model):
        """Продати авто клієнту"""
        if model in self.cars:
            car = self.cars[model]
            self.cars.remove(model)
            print(f"\n{car}\nпродана клієнту {client}")
        else:
            print(
                f"{model} - на жаль, такої моделі немає в нашому автопарку, "
                f"клієнту {client} ми нічим не допоможемо"
            )


my_cars = CarPark()

my_cars.add("Toyota", "Camry", 2020)
my_cars.add("Nissan", "Tiida", 2011)
my_cars.add("Hyundai", "Tucson", 2021)
my_cars.add("Honda", "Civic", 2019)
my_cars.add("BMW", "X5", 2021)
my_cars.add("Mercedes-Benz", "E-Class", 2018)
my_cars.add("Audi", "A6", 2022)
my_cars.add("Ford", "Focus", 2017)
my_cars.add("Nissan", "Altima", 2020)
my_cars.add("Kia", "Sportage", 2018)

my_cars.display()

my_cars.remove("Tucson")
my_cars.display()
print(f"\n{len(my_cars)}")

found_car = my_cars.search("X5")
print(f"\n{found_car}")

found_car = my_cars.search("CRV")
print(f"\n{found_car}")

my_cars.sell_car("Фокусов А.А", "Focus")
my_cars.sell_car("Це Р.В.", "CRV")
