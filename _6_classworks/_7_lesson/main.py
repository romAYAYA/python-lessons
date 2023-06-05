import requests
import time
import os
import shutil

#
# if __name__ == __name__:
#
#     def update_data():
#         url = 'https://api.binance.com/api/v3/ticker/price?'
#         while True:
#             data = requests.get(url)
#             if data.status_code == 200:
#                 with open('temp/data.txt', mode='w', encoding='utf-8') as file:
#                     file.writelines(str(data.json()))
#                     print('Data written successfully!')
#             else:
#                 print('Failed to fetch data')
#
#             time.sleep(3)
#
#     update_data()


current_path = '.'
top_path = '../temp'

if not os.path.exists(top_path):
    os.mkdir(top_path)

with open(f'{top_path}/temp.txt', mode='a', encoding='utf-8') as file:
    file.write('Python is awesome\n')
