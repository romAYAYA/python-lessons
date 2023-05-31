# TODO пробует совершить какой-то код

try:
    print('Money charged')

    print(1 / 0)

    print('money received')

# TODO всегда ловит любые ошибки

except Exception as error:
    print(error)
    print('Money sent back')

# TODO ловит ошибку ТОЛЬКО при делении на ноль

except ZeroDivisionError as error:
    print(error)
    print('Money sent back')

# TODO исполняется всегда

finally:
    # открыли файл - закрыли файл
    print('FINALLY!')

# вызов исключения

try:
    def div2(a, b):
        if b == 0:
            # вызов исключения
            raise Exception
        result = a / b
        if result <= 0:
            raise ArithmeticError
        return result


    print(div2(1, -1))

except Exception as error:
    print('ERROR')
    print(error)
