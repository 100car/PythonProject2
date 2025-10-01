# Завдання 1
# Програма складається з трьох потоків. Перший просить в користувача вводити числа, поки не введено
# порожній рядок, та зберігає числа в список. Інші два потоки чекають поки перший завершить
# роботу, і вже потім запускаються. Один рахує суму чисел в списку, інший рахує середнє арифметичне.
# Список чисел, сума та середнє виводяться на екран
import threading
import time


def get_nums(nums):
    """
    Просить користувача вводити числа до тих пір, поки не буде
    введено порожній рядок. Додає числа в переданий список.
    """
    while True:
        num = input("Введіть число для збереження в списку або натисніть Enter: ")
        if num == "":
            return
        nums.append(int(num))


def calculate_sum_only(nums):
    """
    Обчислює суму чисел у списку.

    :param nums: список чисел
    :return: сума чисел
    """
    result = 0
    for num in nums:
        result += num
    return result


def sum_numbers(nums, results: dict):
    """
    Обчислює суму чисел та зберігає її у словник results під ключем 'suma'.

    :param nums: список чисел
    :param results: словник для збереження результату
    """
    print("Функція sum_numbers почала свою роботу.")
    results["Сума"] = calculate_sum_only(nums)
    time.sleep(0.5)
    print("Функція sum_numbers закінчила свою роботу.")


def average_numbers(nums, results: dict):
    """
    Обчислює середнє арифметичне чисел у списку та зберігає у словник results під ключем 'average'.
    Якщо список порожній, записує повідомлення про неможливість обчислення.

    :param nums: список чисел
    :param results: словник для збереження результату
    """
    print("Функція average_numbers почала свою роботу.")
    if len(nums) == 0:
        results["Середнє"] = "Чисел немає, як можна середнє порахувати?"
    else:
        results["Середнє"] = calculate_sum_only(nums) / len(nums)
    time.sleep(0.5)
    print("Функція average_numbers закінчила свою роботу.")


def main():
    results = {}
    my_nums = []

    # Створення потоків
    thread1 = threading.Thread(target=get_nums, args=(my_nums,))
    thread2 = threading.Thread(target=sum_numbers, args=(my_nums, results))
    thread3 = threading.Thread(target=average_numbers, args=(my_nums, results))

    # Запуск першого потоку і очікування його завершення
    thread1.start()
    thread1.join()

    # Запуск інших потоків
    thread2.start()
    thread3.start()
    thread2.join()
    thread3.join()

    # Вивід результатів
    print("Список введених чисел:", my_nums)
    print("Результати обчислень:", results)


if __name__ == "__main__":
    main()
