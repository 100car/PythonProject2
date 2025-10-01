# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.

import threading


def maximum(nums, results: dict):
    print("Функція maximum почала свою роботу.")
    result = max(nums)
    results["max"] = result
    print("Функція maximum закінчила свою роботу.")


def minimum(nums, results: dict):
    print("Функція minimum почала свою роботу.")
    result = min(nums)
    results["min"] = result
    print("Функція minimum закінчила свою роботу.")


def get_nums():
    nums = []
    while True:
        num = input("Введіть число зі списку або натисніть Enter: ")
        if num == "":
            return nums
        nums.append(int(num))


results = {}
my_nums = get_nums()
thread1 = threading.Thread(target=maximum, args=(my_nums, results))
thread2 = threading.Thread(target=minimum, args=(my_nums, results))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(results)
