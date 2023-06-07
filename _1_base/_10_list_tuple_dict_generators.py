import random

# TODO простой пример


list1 = [1, 2, 3, 4, 5]
list2 = []

for i in list1:
    res = i ** 2
    list2.append(res)
print(list2)

# TODO простейший пример

list3 = [i ** 2 for i in list1]
print(list3)  # [1,4,9,16,25

# новый массив с проверками на четность

list4 = [1, 2, 3, 4, 5]
list5 = []

for x in list4:
    # if x % 2 == 0:
    #     list5.append(True)
    # else:
    #     list5.append(False)
    list5.append(x % 2 == 0)
print(list5)

list6 = [x % 2 == 0 for x in list1]
print(list6)

# пример с условием

list7_1 = ['p', 'P', 'p', 'P', 'p', 5, 'P']
list7 = ['p', 'P', 'p', 'P', 'p', 'P']

list8 = [x for x in list7 if not x.isupper()]
print(list8)

list9 = [
    f'{x}_'
    for x in list7_1
    if isinstance(x, str) and not x.isupper()
]

print(list8)

# пример для генерации массива словарей

list11 = [1, 2, 3, 45, 6, 75, 74]

list10 = [{f'key_{i}': i} for i in list11 if i % 2 != 0]
print(list10)

print(random.randint(1, 100))

res = random.random()
print(res)
print(round(res * 100), '%')

print(random.choices('abcde'))
print(random.choice('abcde'))


# TODO password generator

def password_generator(chars: str, length: int) -> str:
    if length < 0:
        raise Exception(f'length is {length}')
    return ''.join([random.choice(chars) for _ in range(length)])


chars = 'ASDFlkjhnvbn1234567890)(*&^%$#@!'


def make_passwords(count: int):
    with open('passwords.txt', 'w', encoding='utf-8') as file:
        for i in range(1, count + 1):
            generated_password = password_generator(chars, 32)
            file.write(f'{generated_password}\n')


print(make_passwords(1000))

# TODO tuple comprehension

tuple2 = (x ** 2 for x in [1, 2, 3, 4, 5])
print(tuple2, type(tuple2))
for j in tuple2:
    print(j)

# list comp -> [1, 2, 3, 4, 5] -- for V
# TODO list comp - хранит весь объект в оперативной памяти
var1 = 111
import sys

print(sys.getsizeof(var1))
# 10 * 28 = 280
# tuple comp -> generator
# TODO tuple comp - не помнит предыдущий и не знает следующий, есть только текущий
