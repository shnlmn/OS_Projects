import os
import sys
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

dir = filedialog.askdirectory()

walker = (os.walk(dir))
top = next(walker)[1]
dirs = [x[3:] for x in top]
print(top)
print(dirs)
