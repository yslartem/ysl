def cycle_length(n):
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    if n == 1:
        return 0  
    remainder = 1
    length = 0
    seen = {}
    while remainder not in seen:
        seen[remainder] = length
        remainder = (remainder * 10) % n
        length += 1
    return length - seen[remainder]

max_length = 0
best_d = 0

for d in range(2, 1000):
    cl = cycle_length(d)
    if cl > max_length:
        max_length = cl
        best_d = d

print(f"d = {best_d}, длина цикла = {max_length}")