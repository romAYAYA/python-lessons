import requests


# TODO 1st task

# def plus_two(num_1, num_2):
#     try:
#         return num_1 + num_2
#     except TypeError:
#         return 'Expected data type "int". Try again'
#
#
# print(plus_two(40, 2))

# TODO 2nd task

# def access_list_el(list, id):
#     try:
#         return list[id]
#     except IndexError:
#         return 'Invalid index'
#
#
# list_1 = [1, 2, 3, 4, 5]
#
# print(access_list_el(list_1, 4))
# print(access_list_el(list_1, 5))


# TODO 3rd task

def get_todo(todo_id):
    try:
        url = f'https://jsonplaceholder.typicode.com/todos/{todo_id}'
        res = requests.get(url)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as err:
        return f'Request Error: {err}'
    except ValueError:
        return 'Invalid input'
    except Exception as err:
        return f'Error: {err}'


def write_todo(todo_id):
    todo = get_todo(todo_id)
    if isinstance(todo, dict):
        filename = f'{str(todo_id)}.txt'
        with open(filename, 'w') as file:
            file.write(str(todo))


todo_input_id = int(input('Enter todo id: '))
write_todo(todo_input_id)
