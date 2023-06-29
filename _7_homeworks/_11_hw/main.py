import os
import requests
import tkinter as tk
from tkinter import messagebox
import multiprocessing
import threading


def download_image(image_url, image_path):
    res = requests.get(image_url)
    with open(image_path, 'wb') as file:
        file.write(res.content)


# TODO sync

# def download_images_sync():
#     folder_path = './temp'
#     os.makedirs(folder_path, exist_ok=True)
#
#     for i in range(1, 11):
#         image_url = f'https://picsum.photos/500/500/?random={i}'
#         image_path = os.path.join(folder_path, f'image_{i}.jpg')
#
#         download_image(image_url, image_path)
#
#     messagebox.showinfo('Download Complete', 'Images downloaded synchronously!')


# TODO multiprocessing

# def download_images_multiprocess():
#     folder_path = './temp'
#     os.makedirs(folder_path, exist_ok=True)
#
#     processes = []
#     for i in range(1, 11):
#         image_url = f'https://picsum.photos/500/500/?random={i}'
#         image_path = os.path.join(folder_path, f'image_{i}.jpg')
#
#         process = multiprocessing.Process(target=download_image, args=(image_url, image_path))
#         process.start()
#         processes.append(process)
#
#     for process in processes:
#         process.join()
#
#     messagebox.showinfo('Download Complete', 'Images downloaded with processes!')

# TODO threading

def download_images_thread():
    folder_path = './temp'
    os.makedirs(folder_path, exist_ok=True)

    threads = []
    for i in range(1, 11):
        image_url = f'https://picsum.photos/500/500/?random={i}'
        image_path = os.path.join(folder_path, f'image_{i}.jpg')

        thread = threading.Thread(target=download_image, args=(image_url, image_path))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    messagebox.showinfo('Download Complete', 'Images downloaded with threading!')


window = tk.Tk()
window.title('Image Downloader')

if __name__ == '__main__':
    # в command нужно изменить функцию, которая должна отработать (download_images_sync, download_images_multiprocess,
    # download_images_thread или асинхронная)
    button = tk.Button(window, text='Download Images', command=download_images_thread)
    button.pack(padx=20, pady=10)

    window.mainloop()
