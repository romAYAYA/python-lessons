import re

input_from_user1 = 'qwerty'

input_from_user1.isascii()  # пароль должен быть на английском
input_from_user1.islower()
input_from_user1.isdigit()
input_from_user1.isalpha()

# минимум 12 знаков, максимум 16, маленькая и большая буква, спецсимвол и цифра

pattern = r"^(?=.*[A-Za-z]) (?=.*\d) (?=.*[@$!%*#?&]) [A-Za-z\d@$!%*#?&] {8,}$"
# внутри круглых скобок - требования
# внутри квадратных - разрешение на ввод
# внутри фигурных скобок требуемая длина
#  открывает - ^ закрывает - $

password1 = '11111111'
password2 = '123456456qwery'
password3 = 'Absadfgc1423423@!!'

cond1 = re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", string=password3)

if cond1 is None:
    print('Weak password')
else:
    print('Strong password')

print(cond1, type(cond1))

# TODO Usage example with passwords

# while True:
#     a1 = input('Enter a password:').strip()
#     if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", string=a1):
#         print('Weak password')
#         continue
#     b1 = input('Enter the password again: ').strip()
#     if a1 != b1:
#         print('Passwords doesnt match')
#         continue
#
#     print('Password created')
#     break


# TODO check email

def validate_email(mail: str) -> bool:
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", string=mail) is not None:
        return True
    return False


print(validate_email('admin532452345@gmail.ru'))

phoneRegex1 = re.compile(r'\d-\d\d\d-\d\d-\d\d')