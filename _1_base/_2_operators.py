# TODO арифметические операторы

import math

print(10 + 10)  # сложение
print(10 - 10)  # вычетание

print(10 * 10)  # умножение
print(10 / 10)  # деление
print(15 // 10)  # целочисленное деление (отбрасывает дробную часть)

print(12 % 5)  # остаток от деления 12 / 5 = 5 + 5 + 2
print(12 % 5)  # остаток от деления 12 / 5 = 5 + 5 + 2

print(5 % 2 != 0)  # проверка на нечетность

print(2 ** 4)  # возведение в степень

print(81 ** 0.5)  # извлечение из под корня

print(int(math.sqrt(16)))  # извлечение из под корня с помощью библиотеки

print(math.exp(2))

# TODO сокращенные операторы

seconds = 0
seconds = seconds + 1

print(seconds)

seconds += 5  # increment

print(seconds)

seconds -= 1

print(seconds)

# TODO оператор принадлежности (in) и сравнения (is)

# in

list1 = [1, 2]
val1 = 2
cond3 = val1 in list1  # True

print(cond3)

str1 = 'python'

chr1 = 'p'
chr2 = 'P'

print(chr1 in str1)
print(chr2 in str1)

# is

# Example 1
x = [1, 2, 3]
y = x

# Both x and y refer to the same list object
print(x is y)  # True

# Example 2
a = [1, 2, 3]
b = [1, 2, 3]

# Although the contents are the same, a and b refer to different list objects
print(a is b)  # False

# Example 3
c = "hello"
d = "hello"

# In Python, string literals with the same value refer to the same object
print(c is d)  # True
