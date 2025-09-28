# Завдання 1
# Напишіть гру вгадати число: комп’ютер загадує число від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше. Якщо число вгадане менш ніж за 5 спроб, то переміг користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та програшів у файл
#  завантажити дані – завантажити кількості перемог та програшів
# Реалізуйте все функціями

import json
import random

MAX_ATTEMPTS = 5


def new_game():
    """
    Запускає одну гру "Вгадай число".

    Логіка:
    - комп’ютер загадує випадкове число від 1 до 100;
    - користувач вводить свої припущення;
    - на кожну спробу дається підказка "більше" або "менше";
    - якщо число вгадане до 5 спроб включно → повертає 1 (перемога користувача);
    - якщо після 5 невдалих спроб → повертає 0 (перемога комп’ютера).
    """
    print("\n========= Нова гра для поточного гравця. =========")
    secret_number = random.randint(1, 100)
    counter = 0

    while True:
        counter += 1
        if counter == MAX_ATTEMPTS + 1:
            print(f"Використані всі спроби. Ви не вгадали загадане число {secret_number} і програли!")
            return '0'

        user_input = input(f"Спроба №{counter}. Введіть число від 1 до 100: ")

        if user_input.strip().isdigit():
            num = int(user_input.strip())
        else:
            print("Потрібно було ввести число.")
            continue

        if not 1 <= num <= 100:
            print("Потрібно було ввести число від 1 до 100.")
            continue

        if num == secret_number:
            print(f"Вітаю! Ви вгадали! Загадане число - {secret_number}")
            return '1'
        elif num < secret_number:
            print("Більше!")
        else:
            print("Менше!")

def show_menu(options: list[str]) -> str:
    """
    Виводить список опцій меню користувачу і обробляє його вибір.

    Параметри:
    - options (list[str]): список рядків з можливими варіантами.

    Повертає:
    - Вибрану опцію як рядок (str), або None, якщо вибір некоректний.

    Можливе введення:
    - Цифра порядкового номера опції.
    - Назва опції повністю.
    """
    print("Виберіть, будь ласка, один з варіантів:")
    for i, option in enumerate(options, start=1):
        print(f"\t- {option} ({i})")

    choice = input("Ваш вибір: ").strip()

    # якщо ввів цифру
    try:
        if choice.isdigit():
            choice = options[int(choice) - 1]
    except (ValueError, IndexError):
        return None

    return choice if choice in options else None

def new_user():
    """
    Запитує ім'я нового гравця.

    Повертає:
    - Ім'я гравця як рядок (str).
    """
    user = input("Введіть ім'я гравця: ")
    return user

def load(filename='ugadayka.json'):
    """
    Завантажує дані про результати гравців з JSON-файлу.

    Параметри:
    - filename (str): ім'я файлу для завантаження.

    Повертає:
    - Словник з результатами гравців.
      Формат: { 'ім'я': {'wins': int, 'losses': int}, ... }
    - Повертає порожній словник, якщо файл не знайдено.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def merge_nested_dicts(d1, d2):
    """
    Об'єднує два словники з результатами гравців.

    Параметри:
    - d1, d2: словники формату { 'ім'я': {'wins': int, 'losses': int}, ... }

    Логіка:
    - Для кожного гравця сумує wins і losses.
    - Якщо гравець є лише в одному словнику, його дані додаються без змін.

    Повертає:
    - Новий словник з об’єднаними результатами.
    """
    merged = d1.copy()
    for user, scores in d2.items():
        if user not in merged:
            merged[user] = scores.copy()
        else:
            for key, value in scores.items():
                merged[user][key] = merged[user].get(key, 0) + value
    return merged

def save(current_dict, filename="ugadayka.json"):
    """
    Зберігає результати гравців у JSON-файл.

    Параметри:
    - current_dict: словник з результатами гравців.
    - filename (str): ім'я файлу для збереження.

    Використовує:
    - ensure_ascii=False для коректного збереження українських літер.
    - indent=4 для гарного форматування JSON.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(current_dict, file, indent=4, ensure_ascii=False)

def show_results():
    """
    Виводить результати поточного гравця та, за бажанням, всі результати.

    Логіка:
    - Показує кількість перемог та поразок поточного гравця.
    - Запитує користувача, чи показати всі результати.
    - Якщо користувач підтверджує ('y', 'н', 'так') — друкує всі результати у форматі JSON.
    """

    print(f"Ваш результат: перемог - {current_results[current_user]["wins"]}, поразок - {current_results[current_user]["losses"]}.")
    choice = input("Вивести всі результати? (Y/N): ")
    if choice.lower() in ("y", "н", "так"):
        print(json.dumps(current_results, indent=4, ensure_ascii=False))


# Опції меню для передачі у функцію show_menu
options = ["Зміна гравця", "Нова гра", "Завантажити", "Зберегти", "Показати", "Закінчити"]

# створюємо "нульові" записи
current_results = {}
current_user = "Анонім" # Anonymous
current_results[current_user] = {"wins": 0, "losses": 0}

while True:
    print(f"\nГравець {current_user}!")
    user_choice = show_menu(options)
    # print(user_choice)

    if user_choice == options[0]: # Зміна гравця
        current_user = new_user()

    elif user_choice == options[1]: # Нова гра
        current_result = new_game()
        # додати гравця в поточний словник, якщо його там немає.
        if current_user not in current_results:
            current_results[current_user] = {"wins": 0, "losses": 0}
        # оновити результат гравця в поточному словнику
        if current_result == "1":
            current_results[current_user]["wins"] += 1
        elif current_result == "0":
            current_results[current_user]["losses"] += 1
        else:
            print("Такого не могло бути (або '0', або '1'), але по любому, давайте знову вибирати.")
            continue

    elif user_choice == options[2]: # Завантажити
        previous_dict = load()
        current_results = merge_nested_dicts(current_results, previous_dict)

    elif user_choice == options[3]: # Зберегти
        previous_dict = load()
        current_results = merge_nested_dicts(current_results, previous_dict)
        save(current_results)

    elif user_choice == options[4]: # Показати результат
        show_results()

    elif user_choice == options[5]: # Закінчити
        print("Гру закінчено.")
        show_results()
        break

    else:
        print("Такого не могло бути, але по любому, давайте знову вибирати.")
        continue

print("Вітаємо! Ви нарешті закінчили грати в угадайку. Нагадуємо, що надмірне захоплення азартними іграми може призвести до ігрової залежності.")