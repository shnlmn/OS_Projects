import os
import yaml
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
td = os.getcwd()
struct_file = filedialog.askopenfilename(title="Select Directory Structure Template")
cwd = filedialog.askdirectory(title="Select Target Directory")

hierarchy = yaml.safe_load(open(struct_file))['structure']

for exist_root, exist_dirs, exist_files in os.walk(cwd):
    print(exist_dirs)
exist_dirs_names = [x[3:] for x in exist_dirs]


def num_dir(dir):
    temp_h = {}
    for i, (k, v) in enumerate(dir.items(), 1):
        prefix = str(f"0{i}") if i<10 else i
        if len(v) > 0 and type(v) is not list:
            temp_h.update({f"{prefix}_{k}": num_dir(v)})
        else:
            temp_h.update({f"{prefix}_{k}": []})

    return temp_h


def create_dir(dir, h):
    for k, v in h.items():
        tempd = f"{dir}/{k}"
        try:
            if k[:2].isdigit() and k[3:] in top_dirs_names:
                x_dir = top_dirs[top_dirs_names.index(k[3:])]
                os.rename(f"{dir}/{x_dir}", f"{dir}/{k}")
            else:
                os.mkdir(tempd)
        except FileExistsError:
            pass
        if len(v) > 0:
            create_dir(tempd, v)


new_h = num_dir(hierarchy)
create_dir(new_h)