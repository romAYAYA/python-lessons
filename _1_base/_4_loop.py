# TODO цикл по итераторам for
import datetime
import time

# list_val1 = [1, 2, 3, 4, 5, 6]
#
# for i in list_val1:
#     # тело цикла
#     print(i)
# # конец цикля
#
# for j in 'Python':
#     print(j)
#
# for j in ['roma', 'danila', 'oleg']:
#     print(j)
#
# for i in range(1, 100 + 1, 1):  # range(start, stop, step)
#     print(i)
#
# for j in range(100, 1, -1):
#     print(j)

# TODO for loop usage

# res = 0
#
# for i in range(1, 100+1, 1):
#     res += i
# print(res)

# res = 0
#
# for i in range(0, 1000 + 1, 1):
#     res *= i
# print(res)

# for j in range(10):  # если 1 параметр, то это stop
#     print(j)

# for j in range(5, 10):  # если 2 параметра, то это start, stop
#     print(j)

# for j in range(5, 100 + 1, 1):
#     if j >= 50:
#         break
#
#     if j % 5 == 0:
#         continue  # отсеивает числа, которые делятся на 5 без остатка
#
#     if j % 2 == 0:
#         print('even number:', j)
#     else:
#         print('odd number:', j)
#
# for i in 'Python':
#     if i == 'y':
#         continue
#     print(i)

# dict1 = {
#     'key': 1,
#     'Name': 'Roma',
#     'Job': 'Unemployment',
#     'Age': 20
# }
#
# for i in dict1.keys():
#     print(i)
#
# for i in dict1.values():
#     print(i)
#
# for i in dict1.items():
#     print(i)

# TODO условный цикл (с предусловием / постусловием) while

# index = 1
#
# while index < 10:
#     print(index)
#     index += 1
#
# while True:
#     val = input('Are you 18 or more? ')
#     if int(val) > 18:
#         break

# while True:
#     print('Hello')

# TODO таймер чч:мм:сс -> .exe

seconds = 0
minutes = 0
hours = 0
speed = float(input('Enter speed of "tick": '))

while True:
    seconds += 1
    if seconds > 59:
        minutes += 1
        seconds = 0
    if minutes > 59:
        hours += 1
        minutes = 0
    if hours > 23:
        seconds = 0
        minutes = 0
        hours = 0

    time.sleep(speed)

    # minutes = f'0{minutes}' + str(minutes) if minutes < 10 else minutes

    print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
