# TODO типы данных
from _decimal import Decimal

bool1 = True  # булевые значения в формате правда/ложь
bool2 = False  # булевые значения в формате правда/ложь

int1 = 42  # целочисельнные значения

float1 = 12.0  # значения с плавающей точкой

decimal1 = Decimal(12.0)  # значения с плавающей точкой для высокоточных значений

none1 = None  # отсутствие значения

str1 = 'Python'  # строка - коллекция символьных элементов
str2 = '''Hello, py'''  # строка - коллекция символьных элементов

str3 = 'Python' + str(12.0)  # конкатенация (сложение строк)

str4 = f'Python {str2}'  # интерполяция (вставка разных переменных в строку)

str5 = f'Python \n \t {float1}'
# спец символы (в данном случае перенос строки и табуляция)

print(str5)

bytes1 = b'Python'  # байты - коллекция символьных элементов в виде байтов

list1 = [10, True, [], b'Python']  # список - коллекция элементов
list1.append(42)
print(list1)

tuple1 = (12, False)  # кортеж - коллекция неизменяемых элементов

set1 = {42, False, 12}  # множество - коллекция уникальных элементов
set1.add(True)
print(set1)

dict1 = {
    'Name': 'Roma',
    'Job': 'Unemployment',
    'Age': 20,
    'dict2': {
        'name': 'Bogdan',
        'Job': 'Web dev',
        'arr': [10, True, [], b'Python']
    }
}  # словарь - коллекция уникальных элементов в формате ключ-значения

dict3 = {}
int10 = 12.0
print(type(int10))
print(type(dict3))

INT_CONSTANT = 12  # условно-неизменяемая
print(INT_CONSTANT / 12)  # 1.0 float
print(INT_CONSTANT // 12)  # 1 - целочисленное деление

INT_CONSTANT = 15  # AYAYA! Так делать плохо!
print(INT_CONSTANT)

is_commit = False  # можно изменить

IS_COMMIT = False  # нельзя изменить

# TODO действия с переменными

# вывод значений переменных в консоль

type_bool1 = type(bool1)
print(type_bool1)
print(type(bool1))

# проверка принадлежности типа данных

print(isinstance(bool1, str))
print(isinstance(bool1, bool))

# конвертация типов данных

float_to_int1 = int(10.5)  # int()

int_to_float1 = float('10.01')  # float()

str_to_float1 = float('10.2')  # float()

int_to_str1 = str(10.4)  # str()

int_to_bool1 = bool(0)  # bool()
# ...

# получение элементов из коллекции

source_str1 = 'Python is awesome'
print(source_str1[4])
print(source_str1[-1])

source_list1 = [1, 2, 3, 4, 5, 6, 7, 8]

source_list1[3] = 42

print(source_list1[3])

source_list2 = source_list1[2:5:2]  # [start:stop:step]

print('Roma'[::-1])
print(source_list2)
print(source_list1)

dict3 = {
    'name': 'Roma',
    'job': 'Unemployment',
    'age': 20,
}

print(dict3['age'])
dict3['phone'] = '88005553535'

del dict3['name']

print(dict3)
