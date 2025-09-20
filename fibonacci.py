stop = 4000000
a, b = 1, 2
summa = 0

while a <= stop:
    if a % 2 == 0:
        summa += a
    a, b = b, a + b

print(summa)