# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное число N 
# – количество элементов в массиве.  В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

from random import randint
n = int(input('Введите количество элементов n: '))
A = [randint(0,20)for i in range (n)]
print(A)
x = int(input('Введите число х: ')) 
result = abs(x-A[0])
for i in range(n):
    if abs(x-A[i]) < result:
        result = A[i]
print(result)