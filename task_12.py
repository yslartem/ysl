n = float(input("Ваше число: "))
choice = input("Перевести в bytes или kb? ")

if choice == 'bytes':
    print(int(n * 1024), "байт")
elif choice == 'kb':
    print(n / 1024, "килобайт")