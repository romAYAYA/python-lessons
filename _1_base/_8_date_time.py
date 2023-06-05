import time
import datetime
import sys

# timestamp - число отображения количества секунд от 1970 года

var_str = '1234'
var_int = 1234

var_size_str = sys.getsizeof(var_str)
var_size_int = sys.getsizeof(var_int)

print(var_size_str)
print(var_size_int)

print(datetime.datetime.now())

print(datetime.datetime.now())

print(ord('P'))

now1 = datetime.datetime.now()
now2 = now1.strftime('%A %B %m-%d-%y, %H:%M:%S')

print(now1, type(now1))
print(now2, type(now2))

print('stopped')
time.sleep(2.5)
print('hi')
