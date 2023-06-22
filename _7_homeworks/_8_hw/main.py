import re
import requests
from collections import Counter


# TODO 1st task

# def register_user(user_login: str, user_password: str) -> str:
#     while not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", user_login):
#         print('Invalid email format')
#         user_login = input('Enter the email again: ').strip()
#
#     while True:
#         if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", user_password):
#             print('Weak password')
#             user_password = input('Enter the password again: ').strip()
#             continue
#
#         confirm_password = input('Confirm password: ').strip()
#         if user_password != confirm_password:
#             print('Passwords do not match')
#             continue
#
#         return 'Something went wrong. Rerun the program'

# TODO task 2

# def get_even_posts() -> list:
#     url = 'https://jsonplaceholder.typicode.com/posts/'
#     data = requests.get(url)
#     posts_list = data.json()
#     even_posts_list = [post for post in posts_list if post['id'] % 2 == 0]
#     return even_posts_list

# TODO task 3

# def sum_squares() -> int:
#     numbers = []
#     while True:
#         num = int(input("Enter a number: "))
#         numbers.append(num)
#         if sum(numbers) == 0:
#             break
#
#     sum_of_squares = sum([num ** 2 for num in numbers])
#     return sum_of_squares

# TODO task 4


# def calculate_grades(numbers):
#     if all(2 <= num <= 5 for num in numbers):
#         count_fives = numbers.count(5)
#         count_fours = numbers.count(4)
#         count_threes = numbers.count(3)
#         count_twos = numbers.count(2)
#         average_score = sum(numbers) / len(numbers)
#         return (count_fives, count_fours, count_threes, count_twos, average_score)
#     else:
#         return None


# TODO task 5

def calculate_grades(numbers):
    if all(2 <= num <= 5 for num in numbers):
        replaced_numbers = [num if num != 2 else 3 for num in numbers]
        count_fives = replaced_numbers.count(5)
        count_fours = replaced_numbers.count(4)
        count_threes = replaced_numbers.count(3)
        count_twos = replaced_numbers.count(2)
        average_score = sum(replaced_numbers) / len(replaced_numbers)
        return (count_fives, count_fours, count_threes, count_twos, average_score)
    else:
        return None


if __name__ == '__main__':
    # todo task 1
    # login = input('Enter new login: ')
    # password = input('Enter new password: ')
    # print(register_user(login, password))

    # todo task 2
    # print(get_even_posts())

    # todo task 3

    # sum_of_squares = sum_squares()
    # print("Sum of squares:", sum_of_squares)

    # todo task 4, 5
    while True:
        grades_input = input("Enter the grades separated by a space: ")
        grades = [int(grade) for grade in grades_input.split()]
        result = calculate_grades(grades)
        if result is not None:
            break
        else:
            print("Invalid grades entered. All grades should be between 2 and 5.")

    print(f"{result[0]} {result[1]} {result[2]} {result[3]}")
    print(result[4])
