a = list(map(int, input("Элементы списка a через пробел: ").split()))

b = list(map(int, input("Элементы списка b через пробел: ").split()))

res = [x for x in a if x not in b]

print(res)
