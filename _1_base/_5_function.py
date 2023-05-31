from functools import partial


# TODO функции

# def - define - определить

def hi():
    print('hi')


print(hi())


# грязная функция
# def twice_value1(val1, val2):
#     result = val1 + val2
#     print(result)
#
#
# twice_value1(12, 13)


# чистая функция
def twice_value2(val1, val2):
    result = val1 ** val2
    return result  # возврат значения


res1 = twice_value2(10, 3)  # позиционные аргументы
print(res1)


def sum_arr(start, stop):
    """
    # docstring

    :param start: начало для сложения
    :param stop: окончание массива для сложения (включительно)
    :return: возврат результата всех действий
    """

    result = 0
    for i in range(start, stop + 1):
        result += i
    return result


res2 = sum_arr(start=1, stop=12)  # именные аргументы (рекомендуется к употреблению)
print(res2)


def square(val1, val2=2):  # функция с дефолтным аргументом
    # 50 строк кода

    """
    :param val1: исходное число, которое будет возводиться в квадрат
    :param val2: степень числа
    :return: возврат результата всех действий
    """

    return val1 ** val2


print(square(4, 2))
print(square(4))


# DRY - dont repeat yourself

# def - создание функции

# TODO типизация

# Python (CPython) - динамическая сильная типизация ( +скорость разработки, -скорость работы )
# C++ - статическая типизация ( -скорость разработки, +скорость работы )

def divide(val1: float | int, val2: float | int) -> int | float:
    result = val1 / val2
    return result


res = divide(6, 2)
print(res)

list_numbers: list[int] = [1, 2, 3, 4, 5]

for i in list_numbers:
    print(i + 2)


# TODO анонимные функции (lambda)

def multi(a, b):
    return a * b


print(multi(3, 3))

multi2 = lambda a, b: a * b

print(multi(7, 8))


def div1(a, b):
    return a / b


div2 = lambda a, b: a / b

elems = [1, 12, 2, 9, 8]
print(sorted(elems, reverse=False))

people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20}
]


def get_age(person):
    return person['age']


sorted_people = sorted(people, key=get_age)
print(sorted_people)

sorted_people = sorted(people, key=lambda person: person['name'])
print(sorted_people)


# TODO рекурсивные функции
# Python - мультипарадигмальный язык

# процедурный (код - портянка сверху вниз, справа налево)
# ООП - объектно-ориентированный (сущности-объекты и взаимодействие между ними - Ячейка, Строки, Лист, Рабочая книга)
# Функциональный - (очень математический - нет циклов (рекурсия), нет грязных функций), Haskell

def while_counter(value_from):
    # while value_from > 0:
    #     print(value_from)
    #     value_from -= 1
    # print('stop')

    for i in range(value_from, 0, -1):
        print(i)


while_counter(10)


def recursion_counter(value_from):
    print(value_from)
    if value_from <= 1:
        return 1
    else:
        recursion_counter(value_from - 1)


recursion_counter(10)


def recursion_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recursion_factorial(n - 1)


print(recursion_factorial(5))


def while_factorial(n):
    counter = 1
    while n > 0:
        counter *= n
        n -= 1
    return counter


print(while_factorial(5))


def recursion_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursion_sum(n - 1)


print(recursion_sum(23))


def while_sum(n):
    result = 0
    while n > 0:
        result += n
        n -= 1
    return result


print(while_sum(534))


def is_palindrome1(text: str) -> bool:
    return text == text[::-1]


def is_palindrome2(text: str) -> bool:
    if len(text) < 1:
        return True

    if text[0] == text[-1]:
        return is_palindrome2(text[1:-1])
    else:
        return False


str5 = 'madam'

print(is_palindrome1(str5))
print(is_palindrome2(str5))

# TODO области видимости

res2 = 'hi'  # глобальная область видимости


def sym1():
    global res2  # использование переменной из глобальной области видимости
    res2 = 'by'  # локальная область видимости


local_var = 12  # глобальная область видимости


def multiply(x, y):
    return x * y


double = partial(multiply, 2)
result1 = double(5)
print(result1)
