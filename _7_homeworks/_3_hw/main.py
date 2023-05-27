# TODO task 1

# user_login = 'user'
# user_password = 'qwerty'
#
# login_input = input('Enter your login: ')
# password_input = input('Enter your password: ')
#
# if login_input == user_login and password_input == user_password:
#     print('Authentication completed')
# else:
#     print('Invalid login or password')

# TODO task 2

# input_amount = float(input('Insert amount in KZT: '))
# input_currency = int(input('Choose currency (1 - USD, 2 - EUR, 3 - RUB): '))
#
# converted_amount = None
#
# if input_currency == 1:
#     converted_amount = round(input_amount / 420, 2)
# elif input_currency == 2:
#     converted_amount = round(input_amount / 510, 2)
# elif input_currency == 3:
#     converted_amount = round(input_amount / 5.8, 2)
# else:
#     print('Invalid currency selection')
#
# if converted_amount is not None:
#     print(converted_amount)

# TODO task 3

arr = []

for i in range(1, 1000 + 1):
    arr.append(i)

print(arr)

arr_sqr = []

for j in arr:
    arr_sqr.append(j ** 2)

print(arr_sqr)
