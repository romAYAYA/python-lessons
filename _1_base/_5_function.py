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
