# Напишіть програму для збереження даних про музичні групи у вигляді словника, де ключ – назва групи, значення – список альбомів.
# Напишіть функціонал:
#  додати новий гурт
#  додати новий альбом
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle

import json
import pickle
import os


# --- СЛОВНИК З PINK FLOYD :) ---
bands = {
    "Pink Floyd": [
        "The Dark Side of the Moon (1973)",
        "Wish You Were Here (1975)",
        "Animals (1977)",
        "The Wall (1979)",
        "The Final Cut (1983)"
    ]
}


def add_band(name: str) -> None:
    """Додати новий гурт."""
    if name not in bands:
        bands[name] = []
    else:
        print(f"Гурт '{name}' вже існує!")

def add_album(band: str, album: str) -> None:
    """Додати новий альбом до гурту."""
    if band in bands:
        if album not in bands[band]:
            bands[band].append(album)
        else:
            print(f"Альбом '{album}' вже є у гурта '{band}'!")
    else:
        print(f"Гурт '{band}' не знайдено!")

# --- JSON ---
def save_json(filename: str = 'bands.json') -> None:
    """Зберегти словник bands у JSON."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(bands, file, ensure_ascii=False, indent=4)

def load_json(filename: str = 'bands.json') -> dict:
    """Завантажити дані з JSON та повернути словник.
    Якщо файл не існує – повернути порожній словник.
    """
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# --- PICKLE ---
def save_pickle(filename: str = 'bands.pkl') -> None:
    """Зберегти словник bands у Pickle."""
    with open(filename, 'wb') as file:
        pickle.dump(bands, file)

def load_pickle(filename: str = 'bands.pkl') -> dict:
    """Завантажити дані з Pickle та повернути словник.
    Якщо файл не існує – повернути порожній словник.
    """
    if not os.path.exists(filename):
        return {}
    with open(filename, 'rb') as file:
        return pickle.load(file)


if __name__ == '__main__':
    print("=== Початкові дані (Pink Floyd) ===")
    print(bands)

    # Додаємо новий гурт Deep Purple
    add_band("Deep Purple")
    add_album("Deep Purple", "In Rock (1970)")
    add_album("Deep Purple", "Machine Head (1972)")
    add_album("Deep Purple", "In Rock (1970)")

    print("\n=== Після додавання Deep Purple ===")
    print(bands)

    # Зберігаємо у файли
    save_json("bands.json")
    save_pickle("bands.pkl")

    # Чистимо словник і перевіряємо завантаження
    bands = load_json("bands.json")
    print("\n=== Після завантаження JSON ===")
    print(bands)

    bands = load_pickle("bands.pkl")
    print("\n=== Після завантаження Pickle ===")
    print(bands)