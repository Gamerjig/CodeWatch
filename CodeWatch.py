import tkinter as tk
import time



window = tk.Tk()
window.title("CodeWatch")
window.geometry("500x500")
window.config(bg="#1e1e2f")

start_time = None
running = False

label = tk.Label(window, text="00:00:00", font=("Arial", 48, "bold"), fg="#ffffff", bg="#1e1e2f")
label.pack(pady=50)

def format_time(seconds):
    hrs = seconds // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hrs:02d}:{mins:02d}:{secs:02d}"

def elapsed_seconds():
    if start_time:
        return int(time.time() - start_time)
    return 0

def start():
    global start_time, running
    if not running:
        start_time = time.time() - elapsed_seconds()
        running = True
        start_btn.config(text="Resume")
        update()

def pause():
    global running
    running = False

def reset():
    global running, start_time
    running = False
    start_time = None
    label.config(text="00:00:00")
    start_btn.config(text="Start")

def update():
    if running:
        label.config(text=format_time(elapsed_seconds()))
        window.after(1000, update)

button_frame = tk.Frame(window, bg="#1e1e2f")
button_frame.pack(pady=20)

start_btn = tk.Button(button_frame, text="Start", font=("Arial", 18, "bold"),
                      fg="#ffffff", bg="#4caf50", width=8, command=start)
start_btn.grid(row=0, column=0, padx=10)

pause_btn = tk.Button(button_frame, text="Pause", font=("Arial", 18, "bold"),
                      fg="#ffffff", bg="#f44336", width=8, command=pause)
pause_btn.grid(row=0, column=1, padx=10)

reset_btn = tk.Button(button_frame, text="Reset", font=("Arial", 18, "bold"),
                      fg="#ffffff", bg="#2196f3", width=8, command=reset)
reset_btn.grid(row=0, column=2, padx=10)




window.mainloop()

