import os
import glob

# TODO 1st decision

# def delete_junk(dir):
#     for root, dirs, files in os.walk(dir):
#         for file in files:
#             if file.endswith('junk.json'):
#                 file_path = os.path.join(root, file)
#                 try:
#                     os.remove(file_path)
#                     print(f'Deleted: {file_path}')
#                 except OSError as err:
#                     print(f'Error deleting {file_path}: {err}')
#
#
# dir_path = './temp'
#
# delete_junk(dir_path)

# TODO 2nd decision

# def delete_junk(dir):
#     file_paths = glob.iglob(os.path.join(dir, '**', 'junk.json'), recursive=True)
#     for file_path in file_paths:
#         try:
#             os.remove(file_path)
#             print(f'Deleted: {file_path}')
#         except OSError as err:
#             print(f'Error deleting {file_path}: {err}')
#
#
# dir_path = './temp'
#
# delete_junk(dir_path)

# TODO 3rd decision

path = './temp'

for root, dirs, files in os.walk(path, topdown=True):
    for name in files:
        if name == 'junk.json':
            try:
                p = os.path.join(root, name)
                os.remove(p)
                print('You did it')

            except Exception as err:
                print(err)
