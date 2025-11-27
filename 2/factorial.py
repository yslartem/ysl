def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return "1"
    # Рекурсия: n * factorial(n-1)
    return str(n * int(factorial(n - 1)))

# Тесты
print(factorial(5))   # "120"
print(factorial(0))   # "1"
print(factorial(-1))  # None
print(factorial(25))  # "15511210043330985984000000"