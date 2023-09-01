import re
import os

login_pattern = r'^[a-zA-Z0-9]{4,20}$'
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'

user_login = input('Enter your login: ')
user_password = input('Enter your password: ')

try:
    if not re.match(login_pattern, user_login):
        raise ValueError('Invalid login')
    if not re.match(password_pattern, user_password):
        raise ValueError('Invalid password')

    os.makedirs('user', exist_ok=True)

    with open('./user/user_data.txt', 'a') as file:
        file.write(f'Login: {user_login}\nPassword: {user_password}\n\n\n')

    print('Data saved')
except Exception as err:
    print(f'Error: {err}')
