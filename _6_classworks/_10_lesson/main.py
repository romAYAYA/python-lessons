import datetime


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"Start Time: {start_time}")

        end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"End Time: {end_time}")

        arguments = ', '.join([str(arg) for arg in args] + [f'{key}={value}' for key, value in kwargs.items()])
        print(f'Arguments: {arguments}')

        result = func(*args, **kwargs)
        print(f'Result: {result}')

        with open('temp/data.txt', mode='a', encoding='utf-8') as file:
            file.write(f"Start Time: {start_time}\n"
                       f"End Time: {end_time}\n"
                       f"Arguments: {arguments}\n"
                       f"Result: {result}\n"
                       "-------------------\n")

        return result

    return wrapper


@logging_decorator
def sum_nums(a: int, b: int) -> int:
    return a + b


@logging_decorator
def divide_nums(a: int, b: int) -> int:
    return round(a / b)


@logging_decorator
def mult_nums(a: int, b: int) -> int:
    return a * b


print(sum_nums(5, 3))
print(divide_nums(10, 2))
print(mult_nums(4, 6))
