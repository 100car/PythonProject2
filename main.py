# Завдання 1
# Створіть клас Passenger з атрибутами
#  name – ім’я
#  destination – місце, куди прямує
import typing

class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

# Завдання 2
# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця призначення, виводить інформацію як довго їхали

class Transport:
    def __init__(self, speed):
        if speed <= 0:
            raise ValueError("Швидкість має бути > 0.")
        self.speed = speed

    def move(self, destination, distance):
        time_to_destination = distance / self.speed
        print(f"До місця призначення {destination} доїхали за {time_to_destination:.2f} ГОДИН.")

# Завдання 3
# Створіть клас Bus з атрибутами
#  passengers – список пасажирів(об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які хочуть вийти в даному місці
# (виводить їхню загальну кількість) та викликає батьківський метод move()

class Bus(Transport):
    def __init__(self, speed: float, capacity: int):
        super().__init__(speed)
        self.passengers: typing.List[Passenger] = []
        self.capacity = capacity

    def board_passenger(self, passenger: Passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"{passenger.name} сів у автобус (їде до {passenger.destination})")
        else:
            print(f"Автобус переповнений! {passenger.name} не може сісти.")

    def move(self, destination, distance):
        to_exit = [p for p in self.passengers if p.destination == destination]
        for p in to_exit:
            self.passengers.remove(p)

        print(f"У пункті {destination} виходять {len(to_exit)} пасажирів: {[p.name for p in to_exit]}")
        super().move(destination, distance)


p1 = Passenger("Іван", "Київ")
p2 = Passenger("Оля", "Львів")
p3 = Passenger("Петро", "Київ")
p4 = Passenger("Марія", "Одеса")

bus = Bus(speed=120, capacity=3)

bus.board_passenger(p1)
bus.board_passenger(p2)
bus.board_passenger(p3)
bus.board_passenger(p4)  # переповнено

print("\n--- Поїздка 1 ---")
bus.move("Київ", 480)  # 480 км

print("\n--- Поїздка 2 ---")
bus.move("Львів", 300)

print("\n--- Поїздка 3 ---")
bus.move("Одеса", 500)