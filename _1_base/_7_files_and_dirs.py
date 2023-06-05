import json
import os
import shutil

# TODO работа с папками

print(os.getcwd())

first = os.path.abspath(os.path.dirname(__file__))  # содержит абсолютный пусть к текущему скрипту
print(first)

second = '.'  # Содержит относительный путь к текущему скрипту

third = 'temp\\junk2.txt'  # изоляция символа \n - перенос строки, \t - табуляция
fourth = 'temp/junk2.txt'  # изоляция символа \n - перенос строки, \t - табуляция
fifth = r'temp\junk2.txt'  # изоляция символа \n - перенос строки, \t - табуляция

path = os.path.join(first, third)
print(f'path: {path}')

try:
    os.remove('junk.json')  # удаление файла
except Exception as error:
    print(error)

try:
    os.rmdir('temp')  # удаление пустой папки
except Exception as error:
    print(error)

try:
    shutil.rmtree('temp')  # удаление НЕ пустой папки
except Exception as error:
    print(error)

try:
    os.mkdir('data1')  # создаст папку
except Exception as error:
    print(error)

for filename in os.listdir('.'):
    print(filename)

# try:
#     print(filename.split('.')[-1])
# except Exception as error:
#     pass

# os.rename # переименовать
# os.path.exists()

# shutil.copy()
# shutil.move()

