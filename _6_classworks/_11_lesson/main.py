import json
import threading
import multiprocessing
import requests
import time


def performance_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Function {func.__name__} took {execution_time} seconds to execture')
        return result

    return wrapper


url = 'https://jsonplaceholder.typicode.com/todos/1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


@performance_decorator
def get_single_todo():
    res = requests.get(url=url, headers=headers)
    data = res.json()
    with open('temp/single_todo.json', mode='w', encoding='utf-8') as file:
        json.dump(data, file)


@performance_decorator
def threading_get_todos():
    thread_list = []
    for i in range(1, 10 + 1):
        thread_list.append(threading.Thread(target=get_single_todo(), args=(), kwargs={}))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()


if __name__ == "__main__":
    get_single_todo()
    threading_get_todos()

    pass

# def load_todos():
#     for _ in range(10):
#         get_single_todo()


# load_todos()

# @performance_decorator
# def get_todos():
#     res = requests.get(url='https://jsonplaceholder.typicode.com/todos', headers=headers)
#     data = res.json()[:10]
#     with open('temp/todos.json', mode='w', encoding='utf-8') as file:
#         json.dump(data, file)
#
#
# get_todos()
