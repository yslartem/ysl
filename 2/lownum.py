def find_lowest_int(k1):
    k2 = k1 + 1
    n = 1
    while True:
        if sorted(str(n*k1)) == sorted(str(n*k2)) and n*k1!= n*k2:
            return n
        n += 1

# Тесты
print(find_lowest_int(100))  # 8919
print(find_lowest_int(325))  # 477