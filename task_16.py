n = int(input())
a = list(map(int, input().split()))

b = [0] * n
for guest in range(n):
    stul = a[guest]
    b[stul - 1] = guest + 1 

print(*b)
