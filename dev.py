import tkinter as tk
import subprocess
import os
from tkinter import messagebox

os.system("flatpak install org.videolan.VLC  com.visualstudio.code io.github.shiftey.Desktop io.github.peazip.PeaZip -y")
subprocess.call(['python', 'browserselect.py'])