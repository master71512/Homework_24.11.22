# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input('N = '))
fact = 1
newList = []
for i in range(1, N + 1):
    fact *= i
    newList.append(fact)
print(newList)
