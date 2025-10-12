r = float(input("r: "))
print("d:", 2 * r)

print("Сумма чисел от 100 до 500:", sum(range(100, 501)))

a = int(input("Введите число a (меньше 500): "))
if a < 500:
    print("Сумма чисел от", a, "до 500:", sum(range(a, 501)))