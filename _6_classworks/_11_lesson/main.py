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


def get_single_todo(num: int):
    with open(f'temp/data{num}.json', mode='w', encoding='utf-8') as file:
        json.dump(requests.get(f'https://jsonplaceholder.typicode.com/todos/{num}').json(), file)


def get_10_todos():
    for i in range(1, 10 + 1):
        get_single_todo(i)


@performance_decorator
def threading_get_todos():
    thread_list = []
    for i in range(1, 10 + 1):
        thread_list.append(threading.Thread(target=get_10_todos(), args=(), kwargs={}))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()


@performance_decorator
def multiprocessing_get_todos():
    process_list = []
    for i in range(1, 10 + 1):
        process_list.append(multiprocessing.Process(target=get_10_todos(), args=(), kwargs={}))
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()


if __name__ == "__main__":
    # get_single_todo()
    threading_get_todos()
    # multiprocessing_get_todos()

    pass
