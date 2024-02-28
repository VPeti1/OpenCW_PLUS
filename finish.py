import tkinter as tk
import time
import subprocess

def close_window():
    root.destroy()
    subprocess.call(['python', 'main.py'])

root = tk.Tk()
root.title("Installation Status")

# Create a label with the message
message_label = tk.Label(root, text="Install done")
message_label.pack()

# Schedule the window to close after 2 seconds
root.after(5000, close_window)

root.mainloop()
