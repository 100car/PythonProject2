# Завдання 2
# Використовуючи стек створіть клас EnterNumber для введення числа в рядку
# Атрибути:
#  digits – стек з введеними цифрами

from queue import LifoQueue
import copy

# DIGITS = set("0123456789")

class EnterNumber:
    def __init__(self):
        self.digits = LifoQueue()

# Методи:
#  add(digit) – додати нову цифру, вивести помилку якщо не цифра
#  undo() – видалити останню цифру
#  get_number() – повернути число
#  clear() – очистити стек

    def add(self, digit: str):
        if digit.isdigit() and len(digit) == 1:
            self.digits.put(digit)
        else:
            raise ValueError("Введено не цифру!")

    def undo(self):
        if self.digits.empty():
            raise IndexError("Стек порожній!")

        self.digits.get()

    def get_number(self):
        if self.digits.empty():
            print("Стек порожній!!!")
            return

        number_str: str = ""
        while not self.digits.empty():
            number_str += self.digits.get()

        for char in number_str[::-1]:
            self.digits.put(char)

        # for i in range(len(number_str)-1, -1, -1):
        #     self.digits.put(number_str[i])

        return int(number_str[::-1])

    def clear(self):
        self.digits = LifoQueue()


entry = EnterNumber()
entry.add('1')
entry.add('3')
entry.add('7')
entry.add('9')

print(entry.get_number())

entry.undo()
print(entry.get_number())

entry.clear()
print(entry.get_number())