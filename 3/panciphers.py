from itertools import permutations

def has_prop(num_tuple):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        sub_num = num_tuple[i] * 100 + num_tuple[i+1] * 10 + num_tuple[i+2]
        if sub_num % divisors[i-1] != 0:
            return False
    return True

total_sum = 0
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for perm in permutations(digits):
    if perm[0] == 0:
        continue
    if has_prop(perm):
        num = int(''.join(map(str, perm)))
        total_sum += num

print(total_sum)