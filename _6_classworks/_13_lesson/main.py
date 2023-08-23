import tkinter as tk


# import json
# import os
#
# app = tk.Tk()
# app.title('Button clicked')
#
# label = tk.Label(app, text="Click the button")


# def upload_json():
#     dir_path = 'temp'
#     completed_data = []
#
#     file_list = os.listdir(dir_path)
#
#     for filename in file_list:
#         if filename.endswith('.json'):
#             file_path = os.path.join(dir_path, filename)
#             with open(file_path, 'r') as input_file:
#                 data = json.load(input_file)
#                 completed_data.append(data)
#
#     with open('new_json.json', 'w') as output_file:
#         json.dump(completed_data, output_file, indent=4)
#
#     label.config(text="JSON uploaded from {} files".format(len(completed_data)))

# def upload_json():
#
#
# button = tk.Button(app, text="Click me", command=upload_json)
#
# label.pack()
# button.pack()
#
# app.mainloop()


def decorator_val_to_float(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            result = float(result)

        except Exception as err:
            return err

        return result

    return wrapper


@decorator_val_to_float
def func1(a, b):
    return f"{a}{b}"


@decorator_val_to_float
def func2(a):
    return a ** 2


@decorator_val_to_float
def func3(a):
    return a / 2


@decorator_val_to_float
def func4(a):
    return a / '2'


res1 = func1(1, 2)
print(type(res1), res1)

res2 = func2(2)
print(type(res2), res2)

res3 = func3(1)
print(type(res3), res3)

res4 = func4(1)
print(type(res4), res4)

arr = [1, 2, 3, 4, 5]

print(*arr)

arr2 = [*arr]

arr2.append(7)

print(arr2)
print(arr)
