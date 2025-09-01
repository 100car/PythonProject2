# Завдання 1
# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
#   o CreditCardPayment – оплата карткою {amount}{currency}
#   o PayPalPayment – оплата PayPal {amount}{currency}
#   o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у користувача тип рахунку та потрібні атрибути і повертає
# об’єкт. Створіть декілька рахунків, добавте їх у список та для кожної викличте відповідні методи.

class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"оплата карткою {amount} {self.currency}")

class PayPalPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"оплата PayPal {amount}{self.currency}")

class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"оплата криптогаманцем {amount}{self.currency}")

def create_payment():

    #===================== список (!!!list!!!) доступних опцій ===========
    options = ["CreditCardPayment", "PayPalPayment", "CryptoPayment"]

    try:
        sum_money = float(input("Введіть суму платежу: "))
    except:
        print("Неправильна сума платежу")
        return None

    currency = input("Введіть валюту платежу: ")

    print("Вкажіть тип рахунку.")

    #===================== шаблон імхо буде ==============================
    print("Виберіть, будь ласка, один з варіантів:")
    for i, option in enumerate(options, start=1):
        print(f"\t{option} (або просто введіть {i})")

    choice = input("Ваш вибір: ").strip()

    # Нормалізація: якщо ввів цифру - перетворимо у назву
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(options):
            choice = options[index]

    if choice == "CreditCardPayment":
        return CreditCardPayment(currency), sum_money
    elif choice == "PayPalPayment":
        return PayPalPayment(currency), sum_money
    elif choice == "CryptoPayment":
        return CryptoPayment(currency), sum_money
    else:
        print("Некоректний вибір!")
        return None

payments = []

for _ in range(3):
    result = create_payment()
    if result:
        payments.append(result)

print("\n=== Виклик pay() для всіх рахунків ===")
for payment, amount in payments:
    payment.pay(amount)
