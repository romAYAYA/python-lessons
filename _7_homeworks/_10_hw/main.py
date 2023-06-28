import tkinter as tk
from tkinter import messagebox
import bcrypt


def save_login():
    username = username_entry.get()
    password = password_entry.get()

    if username.strip() == '' or password.strip == '':
        messagebox.showerror('Error', 'Login and password cannot be empy')
        return

    try:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        with open('./temp/login.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Login: {username}\tPassword: {hashed_password}\n')

            messagebox.showinfo('Success', 'Login information saved!')
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

    except Exception as err:
        messagebox.showerror('Error', f'An error occurred: {str(err)}')


window = tk.Tk()
window.title('Registration Form')

window_width = 800
window_height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

username_label = tk.Label(window, text='Login: ')
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text='Password: ')
password_label.pack()
password_entry = tk.Entry(window, show='*')
password_entry.pack()

if __name__ == '__main__':

    save_button = tk.Button(window, text='Save', command=save_login)
    save_button.pack()

    window.mainloop()
