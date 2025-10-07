options = ["CreditCardPayment", "PayPalPayment", "CryptoPayment"]
print("Виберіть, будь ласка, один з варіантів.")
print("Введіть або назву варіанту, або його порядковий номер:")
for i, option in enumerate(options, start=1):
    print(f"\t{option} ({i})")

choice = input("Ваш вибір: ").strip()

if choice.isdigit():
    idx = int(choice) - 1
    if 0 <= idx < len(options):
        choice = options[idx]

if choice not in options:
    print("Некоректний вибір!")
    pass

if choice == options[0]:
    pass
elif choice == options[1]:
    pass
elif choice == options[2]:
    pass

print(f"{choice =}")
