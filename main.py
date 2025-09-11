import DoubleLinkedList

from typing import List
from DoubleLinkedList import DoubleLinkedList

# Завдання 1
# Використовуючи класи з практичної реалізуйте клас Shop з трьома чергами до кас.
# Кожна черга реалізується через двозв’язний список
# Атрибути
#  queue1, queue2, queue3 – черги до кас
# Методи
#  add_buyer(name, idx) – додає покупця в кінець черги номер idx
#  serve_buyer(idx) – обслуговує покупця з черги idx (вивести повідомлення та видалити покупця з черги) Якщо черга
# стала порожньою, то викликати _reorder(idx)
#  _reorder(idx) – з усіх черг останній покупець переходить в чергу з номером idx
#  display_info() – виводить на екран 3 черги

class Shop:
    def __init__(self, num_of_queues: int):
        self.num_of_queues = num_of_queues
        self.queues: List[DoubleLinkedList] = [DoubleLinkedList() for _ in range(num_of_queues)]

    def add_buyer(self, name: str, idx: int):
        if 0 < idx <= len(self.queues):
            self.queues[idx-1].push_end(name)
        else:
            raise ValueError("Неправильний номер черги, в яку додаємо покупця.")

    def _reorder(self, idx: int):
        if 0 < idx <= len(self.queues):
            moved = False
            for num in range(len(self.queues)):
                if num != idx - 1:
                    last_in_que = self.queues[num].pop_end()
                    if last_in_que is not None:
                        self.queues[idx - 1].push_end(last_in_que)
                        moved = True
            if moved:
                print(f"З усіх черг останні покупці попереходили у чергу з номером {idx}.")
        else:
            raise ValueError("Неправильний номер черги, яка реорганізується.")

    def serve_buyer(self, idx: int):
        if 0 < idx <= len(self.queues):
            buyer = self.queues[idx - 1].pop_start()
            if buyer is None:
                print(f"Черга №{idx} порожня, обслуговувати нікого.")
            else:
                print(f"В черзі №{idx} обслужили покупця {buyer}.")
                if self.queues[idx - 1].head is None:
                    self._reorder(idx)
        else:
            raise ValueError("Неправильний номер черги під час обслуговування.")

    def display_info(self):
        for index, que in enumerate(self.queues, start = 1):
            print(f"Черга {index}. {que}")
        print()


shop = Shop(3)
shop.add_buyer("Олег", 1)
shop.add_buyer("Марина", 2)
shop.add_buyer("Марія", 2)
shop.add_buyer("Андрій", 3)
shop.add_buyer("Ірина", 1)
shop.add_buyer("Василь", 2)
shop.add_buyer("Тетяна", 3)
shop.add_buyer("Сергій", 3)
shop.add_buyer("Анна", 3)

shop.display_info()
shop.serve_buyer(1)
shop.serve_buyer(2)
shop.serve_buyer(3)
print("Після обслуговування покупців:")
shop.display_info()
# shop.serve_buyer(2)
shop.serve_buyer(1)
shop. display_info()