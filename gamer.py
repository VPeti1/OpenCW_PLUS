import tkinter as tk
import subprocess
import os
from tkinter import messagebox

os.system("flatpak install org.videolan.VLC  com.valvesoftware.Steam com.discordapp.Discord io.github.peazip.peazip -y")
subprocess.call(['python', 'browserselect.py'])