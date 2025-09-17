# Завдання 3
# Створіть дочірні класи від Zone та перевизначте метод serve_passenger() щоб він повертав пару:
# пасажир та True/False в залежності від успішності перевірки.
# Перевірки:
#  реєстрація – наявність білету (у багажі)
#  безпека – відсутність небезпечних предметів у багажі: ніж, зброя, вибухівка
#  посадка – перевірка не потрібна
# Для цього скористайтесь класом Passenger
# Атрибути:
#  name – ім’я
#  priority – пріоритет
#  baggage – список з предметами в багажі

from queue import PriorityQueue


class Passenger:
    def __init__(self, name, priority, baggage=None):
        if baggage is None:
            baggage = []
        self.name = name
        self.priority = priority
        self.baggage = baggage

    def __lt__(self, other):
        """Порівняння пасажирів за пріоритетом (для PriorityQueue)."""
        return self.priority < other.priority

    def __str__(self):
        return f"Пасажир {self.name}, пріоритет={self.priority}, багаж={self.baggage}"


class Zone:
    def __init__(self, name):
        self.name = name
        self.passengers = PriorityQueue()

    def add(self, passenger: Passenger):
        self.passengers.put((passenger.priority, passenger))

    def serve_passenger(self):
        if self.passengers.empty():
            return None, False
        priority, passenger = self.passengers.get()
        # Базовий клас нічого не перевіряє, дочірні нижче
        return passenger, True

    def __len__(self):
        return self.passengers.qsize()


# --------------------------
# Дочірні класи
# --------------------------

class RegistrationZone(Zone):
    def serve_passenger(self):
        if self.passengers.empty():
            return None, False
        priority, passenger = self.passengers.get()
        success = "ticket" in passenger.baggage
        print(f"{passenger.name} проходить реєстрацію -> {'OK' if success else 'FAIL'}")
        return passenger, success


class SecurityZone(Zone):
    DANGEROUS = {"knife", "gun", "explosives"}

    def serve_passenger(self):
        if self.passengers.empty():
            return None, False
        priority, passenger = self.passengers.get()
        dangerous_items = [item for item in passenger.baggage if item in self.DANGEROUS]
        success = not dangerous_items
        print(f"{passenger.name} проходить контроль безпеки -> {'OK' if success else 'FAIL'}")
        return passenger, success


class BoardingZone(Zone):
    def serve_passenger(self):
        if self.passengers.empty():
            return None, False
        priority, passenger = self.passengers.get()
        # Тут перевірка не потрібна
        print(f"{passenger.name} проходить посадку -> OK")
        return passenger, True


# --------------------------
# Airport
# --------------------------

class Airport:
    def __init__(self):
        self.zones = {
            "register": RegistrationZone("Реєстрація"),
            "security": SecurityZone("Контроль безпеки"),
            "boarding": BoardingZone("Посадка")
        }
        self.finished = []

    def add(self, passenger: Passenger):
        self.zones["register"].add(passenger)

    def serve_registration(self):
        passenger, ok = self.zones['register'].serve_passenger()
        if ok and passenger:
            self.zones['security'].add(passenger)

    def serve_security_control(self):
        passenger, ok = self.zones['security'].serve_passenger()
        if ok and passenger:
            self.zones['boarding'].add(passenger)

    def serve_boarding(self):
        passenger, ok = self.zones['boarding'].serve_passenger()
        if ok and passenger:
            print(f"{passenger.name} сів на літак")
            self.finished.append(passenger)

    def show_statistics(self):
        print("\nСтатистика аеропорту:")
        for key, zone in self.zones.items():
            print(f"- {zone.name}: {len(zone)} пасажирів у черзі")
        print(f"- Пройшли всі етапи та сіли в літак: {len(self.finished)} пасажирів")

# TASK3

passenger1 = Passenger("Alice", 2, ["ticket", "phone"])
passenger2 = Passenger("Bob", 1, ["ticket", "knife"])
passenger3 = Passenger("Charlie", 3, ["ticket"])
passenger4 = Passenger("David", 4, ["ticket", "laptop"])
passenger5 = Passenger("Eva", 2, ["bottle", "knife"])
passenger6 = Passenger("Frank", 3, ["book"])
passenger7 = Passenger("Grace", 1, ["ticket", "explosives"])
passenger8 = Passenger("Hannah", 5, ["phone", "tablet"])
passenger9 = Passenger("Ivy", 2, ["ticket", "earphones"])
passenger10 = Passenger("Jack", 1, ["ticket", "gun"])

# Створюємо аеропорт
airport = Airport()

# Додаємо пасажирів до реєстрації
airport.add(passenger1)
airport.add(passenger2)
airport.add(passenger3)
airport.add(passenger4)
airport.add(passenger5)
airport.add(passenger6)
airport.add(passenger7)
airport.add(passenger8)
airport.add(passenger9)
airport.add(passenger10)

# Проходимо етапи для кожного пасажира
for _ in range(10):
    airport.serve_registration()
    airport.serve_security_control()
    airport.serve_boarding()

# Показуємо статистику
airport.show_statistics()