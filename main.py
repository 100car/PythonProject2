# Завдання 1
# Напишіть клас Банківський рахунок з атрибутами:
#  ім'я клієнта
#  баланс
#  валюта
#  словник з курсом валют(однаковий для всіх)
# Додайте методи:
#  вивід загальної інформації
#  перевірка чи відома валюта(якщо ні, викликати ValueError)
#  перевести гроші з однієї валюти в іншу(ця операція часто використовується, тому зручно реалізувати окремим методом)
#  зміна валюти
#  поповнення балансу(валюта та сама)
#  зняття грошей з балансу(валюта та сама).
from types import new_class

# https://bank.gov.ua/ua/markets/exchangerates + гривня). Де три, там усі:
CURRENCY_RATES = {
    "UAH": 1,
    "AUD": 26.5105,
    "AZN": 24.2804,
    "DZD": 0.31813,
    "THB": 1.26463,
    "BGN": 24.4994,
    "KRW": 0.029683,
    "HKD": 5.2814,
    "DKK": 6.4182,
    "AED": 11.2398,
    "USD": 41.2839,
    "VND": 0.0015654,
    "EUR": 47.91,
    "EGP": 0.8517,
    "JPY": 0.2776,
    "PLN": 11.2389,
    "INR": 0.47163,
    "CAD": 29.6761,
    "GEL": 15.2621,
    "LBP": 0.000461,
    "MYR": 9.7674,
    "MXN": 2.2036,
    "MDL": 2.4541,
    "ILS": 12.143,
    "NZD": 23.9736,
    "NOK": 4.0483,
    "ZAR": 2.3415,
    "RON": 9.481,
    "IDR": 0.0025249,
    "SAR": 11.002,
    "RSD": 0.40885,
    "SGD": 32.0353,
    "BDT": 0.33979,
    "KZT": 0.076819,
    "TND": 14.2363,
    "TRY": 1.0066,
    "HUF": 0.121014,
    "GBP": 55.3824,
    "CZK": 1.9494,
    "SEK": 4.286,
    "CHF": 51.0687,
    "CNY": 5.75,
    "XDR": 56.3098
}

class BankAccount:
    def __init__(self, client_name, balance, currency, currency_dict = None):
        self.client_name = client_name
        self.balance = balance
        self.currency = currency
        self.currency_dict = CURRENCY_RATES

    def show_info(self):
        print()
        print("Інформація про рахунок:")
        print(f"\tІм'я клієнта: {self.client_name}")
        print(f"\tБаланс: {self.balance:.2f} {self.currency}")

    def is_currency_supported(self, currency):
        if currency not in self.currency_dict:
            raise ValueError(f"Нацбанк України не працює з '{currency}'.")
        else:
            return True

# Розглядаю "перевести гроші з однієї валюти в іншу" як "вирахувати, обчислити, скільки це буде грошей в іншій валюті"
# Валюта при цьому не змінюється, чисто інформативно
    def calculate_currency(self, calculated_currency):
        try:
            if self.is_currency_supported(calculated_currency):
                old_rate = self.currency_dict[self.currency]
                new_rate = self.currency_dict[calculated_currency]
                return self.balance * old_rate / new_rate
            return None
        except ValueError as error:
            print(f"Помилка: {error}")
            return None

    def convert_currency(self, new_currency):
        self.balance = self.calculate_currency(new_currency)
        self.currency = new_currency

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Рахунок {self.client_name} поповнено на {deposit_amount} {self.currency}")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("На рахунку не вистачає коштів!")
        else:
            self.balance -= withdraw_amount
            print(f"З рахунку {self.client_name} знято {withdraw_amount} {self.currency}")



my_account1 = BankAccount("Коваль Олена Миколаївна", 10000, "UAH")
my_account1.show_info()

my_account2 = BankAccount("Шевченко Олександр Олександрович", 1000, "USD")
my_account2.show_info()

#if my_account2.is_currency_supported("JPY"):
#    print("Є така валюта.")
#if my_account2.is_currency_supported("ПШИК"):
#    print("Є така валюта.")

my_account3 = BankAccount("Бондаренко Андрій Іванович", 5000, "JPY")
my_account3.show_info()
# print(my_account3.calculate_currency("UAH"))
# my_account3.show_info()
# print(my_account3.calculate_currency("JPY"))
# my_account3.show_info()
# print(my_account3.calculate_currency("JPW"))
# my_account3.show_info()
my_account3.convert_currency("USD")
my_account3.show_info()
my_account3.convert_currency("гривня")

my_account4 = BankAccount("Ткаченко Наталія Василівна", 3000, "EUR")
my_account4.show_info()
my_account4.deposit(500)
my_account4.show_info()

my_account5 = BankAccount("Коваленко Володимир Петрович", 15000, "PLN")
my_account5.show_info()
my_account5.withdraw(19000)
my_account5.withdraw(9000)
my_account5.show_info()


#################################################### Лабораторна робота. Модуль 11. ООП. Тема: ООП. Частина 2. (Практична 11.2.pdf) ####################################################

# Завдання 3
# Створіть клас Автомобіль з атрибутами:
#  марка
#  пробіг
#  рівень пального
#  витрата пального(л/км)
#  чи є справним(за замовчуванням True)
# Реалізуйте методи:
#  проїхати певну відстань, має змінитись пробіг та рівень пального, якщо автомобіль справний та достатньо пального
# З ймовірністю 40% автомобіль може зламатись
#  ремонт
#  поповнення пального

# import random
#
# class Car:
#     def __init__(self, car_brand, odometer, current_fuel, fuel_per_100km, is_working = True):
#         self.car_brand = car_brand
#         self.odometer = odometer
#         self.current_fuel = current_fuel
#         self.fuel_per_100km = fuel_per_100km
#         self.is_working = is_working
#
#     def travel(self, travel_distance):
#         if not self.is_working:
#             print("Автомобіль не працює!!!")
#             return
#         elif self.fuel_per_100km * travel_distance / 100 > self.current_fuel:
#             print(f"Щоб проїхати {travel_distance} км, не вистачить пального!!!")
#             return
#         else:
#             self.current_fuel -= self.fuel_per_100km * travel_distance / 100
#             self.odometer += travel_distance
#             if random.random() < 0.4:
#                 self.is_working = False
#
#     def repair(self):
#         if not self.is_working:
#             print("Автомобіль на ремонті!!!")
#
#     def add_fuel(self, liters):
#         if liters < 0:
#             print("Пальне не можна зливати!!")
#             return
#         else:
#             self.current_fuel += liters
#
#
#     def show_info(self):
#         print(self.car_brand, self.odometer, self.current_fuel, self.fuel_per_100km, self.is_working)
#
# my_car = Car("Nissan", 100000, 40, 7.0)
# my_car.show_info()
#
# my_car.travel(1000)
# my_car.show_info()
#
# my_car.travel(200)
# my_car.repair()
# my_car.show_info()
#
# my_car.add_fuel(-40)
# my_car.add_fuel(30)
# my_car.show_info()



# Завдання 1
# Створіть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі та список під-задач
#  виконати задачу, передається назва, час та ціна виконання
#  поповнення кошторису

# опис класу
# (шаблон який описує всі проекти)
# class Project:
#     def __init__(self, name: str, budget: int, tasks: list):
#         self.name = name
#         self.budget = budget
#         self.tasks = tasks
#
#         self.expenses = 0
#         self.is_finished = False
#         self.time = 0
#
#     def show_info(self):
#         print()
#         print(f"Інформація по проекту {self.name}")
#         print(f'\t Бюджет -- {self.budget}грн')
#         print(f"\t Використано -- {self.expenses}/{self.budget}")
#         print(f"\t Час виконання -- {self.time} місяців")
#
#         if self.is_finished:
#             print(f'\t Статус -- Завершений')
#         else:
#             print(f'\t Статус -- Незавершений')
#
#         print('\t Список задач:')
#         for task in self.tasks:
#             print(f"\t\t {task}")
#
#     def add_task(self, new_task):
#         self.tasks.append(new_task)
#         print(f"Додано нове завдання {new_task}")
#
#     def create_subtasks(self, old_task, subtasks):
#         # чи є стара задачі в списку
#         if old_task not in self.tasks:
#             print(f"Такої задачі немає в списку")
#             return
#
#         # old_task є в списку
#         self.tasks.remove(old_task)
#         self.tasks.extend(subtasks)  # добавити всі елементи з subtasks в список self.tasks
#
#         # # спосіб де багато відступів
#         # if old_task in self.tasks:
#         #     # old_task є в списку
#         #     self.tasks.remove(old_task)
#         #     self.tasks.extend(subtasks)  # добавити всі елементи з subtasks в список self.tasks
#         # else:
#         #     print(f"Такої задачі немає в списку")
#
#     def do_task(self, task, price, time):
#         if task not in self.tasks:
#             print(f"Такої задачі немає в списку")
#             return
#
#         if price > (self.budget - self.expenses):
#             print('Не вистачає коштів')
#             return
#
#         # все добре, робимо задачу
#         self.tasks.remove(task)
#         self.expenses += price
#         self.time += time
#
#         self.is_finished = len(self.tasks) == 0
#
#     def deposit(self, price):
#         self.budget += price
#
#
#
#
# # створення конкретного проекту
# project1 = Project('Making Film', 10000, ['write plot', 'find actors'])
# project2 = Project('Create Site', 5000, ['create name', 'create database'])
#
# project1.show_info()
#
# project1.add_task("find location")
# project1.show_info()
# print(project1.tasks)
#
#
# project1.create_subtasks('talk with producer', [])
#
# project1.create_subtasks("find actors",
#                          ['talk with actor1', 'talk with actor2'])
# project1.show_info()
#
# project1.do_task('talk with actor1', 1000, 0.5)
# project1.show_info()
#
# project1.do_task('write plot', 20000, 3.5)
#
# project1.deposit(50000)
# project1.do_task('write plot', 20000, 3.5)
# project1.show_info()
#
#
#
# # створення конкретного проекту
# project1 = Project("Making Film", 1000, ['write pilot', 'find actors'])
#
# project1.show_info()
# project1.add_task("find location")
# project1.show_info()
# #
# # Завдання 2
# # Створіть клас Телефон з атрибутами:
# #  максимальний обсяг пам’яті
# #  зайнята пам’ять
# #  чи включений(за замовчуванням False)
# #  встановлені додатки у вигляді словника, де ключ – назва додатку, значення – обсяг пам’яті
# # Додайте методи:
# #  вивести інформацію про використання пам’яті
# #  видалити додаток
# #  встановити новий додаток, якщо пам’яті достатньо
# #  оновити додаток(нова версія може займати іншу кількість пам’яті)
# #  запустити додаток, якщо він є і якщо телефон вкючений
# #  включити телефон
# #  виключити телефон
#
# class Telephone:
#     def __init__ (self, max_memory, used_memory):
#         self.max_memory = max_memory
#         self.used_memory = used_memory
#         self.is_poweron = False
#         self.apps = {}
#
#     def show_memory_usege(self):
#         print(f'виористано памяті {self.used_memory} Mb')
#         print(f'Максимальеий обсяг памяті -- {self.max_memory} Mb')
#         print('Додатки: ')
#         for app in self.apps:
#             print(f'\t {app} - {self.apps[app]} Mb')
#
#         print()
#
#     def remove_app(self, old_app):
#         if old_app not in self.apps:
#             print('додаток відсутній')
#             return
#
#         self.used_memory -= self.apps[old_app]
#         self.apps.pop(old_app)
#
#     def add_app(self, name_app, app_memory):
#         if name_app in self.apps:
#             print('Програма є')
#             return
#
#         if app_memory > self.max_memory - self.used_memory:
#             print('немає памяті')
#             return
#
#         self.apps[name_app] = app_memory
#         self.used_memory += app_memory
#
#     def update_app(self, update_app, memory):
#         if update_app not in self.apps:
#             print('Програма немає')
#             return
#
#         update_mem = self.apps[update_app]
#
#         self.used_memory -= update_mem
#         self.used_memory += memory
#         self.apps[update_app] = memory
#
#     def start_app(self, app):
#         if app not in self.apps:
#             print('додатку немає')
#             return
#
#         if not self.is_poweron:
#             print('Телефон виключений')
#             return
#
#         print("додаток запущено")
#
#     def turn_on(self):
#         self.is_poweron = True
#
#     def turn_off(self):
#         self.is_poweron = False
#
#
#
# telefone = Telephone(30000, 0)
# telefone.show_memory_usege()
# telefone.remove_app('youtube')
# telefone.show_memory_usege()
# telefone.add_app('tiktok', 5000)
# telefone.show_memory_usege()
# telefone.update_app('tiktok', 6000)
# telefone.show_memory_usege()
# telefone.start_app('tiktok')
#
# telefone.turn_on()
# telefone.start_app('tiktok')





