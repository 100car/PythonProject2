# Завдання 1
# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass
import abc

# При перевірці ШІ, чат GPT стверджує, що я хотів створити абстрактний клас, то нехай буде
class Pet(abc.ABC):
    def __init__(self, name, satiety = 50, energy = 50):
        if not 0 <= satiety <= 100:
            raise ValueError("Рівень ситості має бути від 0 до 100.")
        elif not 0 <= energy <= 100:
            raise ValueError("Рівень енергії має бути від 0 до 100.")
        else:
            self.name = name
            self.satiety = satiety
            self.energy = energy

    def sleep(self):
        print("Після сну рівень енергії становить 100.")
        self.energy = 100

    def eat(self, food_amount):
        change = min(100 - self.satiety, food_amount)
        self.satiety += change
        print(f"{self.name} поїв. Рівень ситості: {self.satiety}")

    @abc.abstractmethod
    def play(self, activity_level):
        raise  NotImplementedError("Цей метод буде реалізовано в підкласі чи підкласах.")

    def make_sound(self):
        pass

# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо energy > 30, ловить мишу. Якщо satiety > 40, то грається з мишею, інакше їсть


class Cat(Pet):
    def play(self, activity_level):
        if self.satiety > 60:
            self.energy = max (self.energy - 2 * activity_level, 0)
            self.satiety = max (self.satiety - activity_level, 0)
            # print(f"{self.satiety =}, {self.energy =}")

    def make_sound(self):
        print("Мяу")

    def catch_mouse(self):
        if self.energy <= 30:
            print(f"{self.name} не зміг спіймати мишку, його ({self.energy=}.)")
        else:
            print(f"{self.name} спіймав мишку ", end="")
            if self.satiety > 40:
                print("і грається з нею.")
            else:
                print("і їсть бідного гризуна.")


# Тестування 1
# tuzik = Pet("Тузик", 50, 100)
# julbars = Pet("Джульбарс", 100, 100)
# sirko = Pet("Сірко")
# murchik = Cat("Мурчик", energy=70, satiety=80)
# print(murchik.satiety, murchik.energy)
# murchik.play(70)
# print(murchik.satiety, murchik.energy)

# Тестування 2
# murchik = Cat("Мурчик", energy=70, satiety=80)
# murchik.make_sound()
# murchik.play(30)
# murchik.catch_mouse()
# murchik.sleep()
# murchik.catch_mouse()

# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на acticity_level//2 та satiety на acticity_level // 2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує energy на 5

class Dog(Pet):
    def play(self, activity_level):
        if self.satiety > 15:
            self.energy = max (self.energy - (activity_level // 2), 0)
            self.satiety = max (self.satiety - (activity_level // 2), 0)
            print(f"{self.satiety =}, {self.energy =}")
        else:
            print(f"{self.satiety =}, {self.name} ненаїжений, щоб гратися")

    def make_sound(self):
        print("Гав!!!")

    def fetch_ball(self):
        if self.satiety > 10:
            self.energy = max(self.energy - 5, 0)
            print(f"{self.name} зловив м’яча, його енергія стала {self.energy}")
        else:
            print(f"{self.satiety =}, {self.name} ненаїжений, щоб ловити м’яча")


tuzik = Dog("Тузик", 50, 100)

# Тестування 3
print(tuzik.satiety, tuzik.energy)
tuzik.play(10)
tuzik.play(40)
tuzik.play(20)
tuzik.play(70)
tuzik.make_sound()
tuzik.fetch_ball()
tuzik.fetch_ball()
tuzik.fetch_ball()
tuzik.fetch_ball()
tuzik.fetch_ball()
tuzik.fetch_ball()
tuzik.fetch_ball()
tuzik.fetch_ball()
tuzik.fetch_ball()
tuzik.fetch_ball()
tuzik.fetch_ball()
tuzik.fetch_ball()
tuzik.fetch_ball()
tuzik.fetch_ball()



