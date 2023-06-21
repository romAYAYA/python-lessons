import tkinter as tk

root = tk.Tk()
root.title("Timer")

time_remaining = 0
is_running = False

label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
label.pack(pady=10)


def start_timer():
    global is_running
    if not is_running:
        is_running = True
        update_timer()


def update_timer():
    global time_remaining
    if is_running:
        label.config(text=format_time(time_remaining))
        time_remaining += 1
        root.after(1000, update_timer)


def format_time(time):
    minutes, seconds = divmod(time, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack()

root.mainloop()
