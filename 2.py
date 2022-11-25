# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1

N = int(input('N = '))
div = N
for i in range(N, 1, -1):
    if N % i == 0:
        div = i
print(div)
