""" Super file organizer by part of the filename """
import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory


# hide root window
root = tk.Tk()
root.withdraw()

# intro explanation pop-up
tk.messagebox.showinfo("info", "Selecione a pasta com os desdobramentos.")

# asks what directory to work with
path_main = askdirectory(
    initialdir="~/downloads", title="Selecione a pasta onde estão os arquivos"
)
names = os.listdir(path_main)

file_types = ["site", "voxus", "GDN", "social", "vtex"]

if not os.path.exists(path_main):
    os.makedirs(path_main)

os.chdir(path_main)


def new_dir(types):
    """creates folder"""

    os.makedirs(types)


# need that code that filters by extention
for site in names:
    each_file = os.path.join(path_main, site)
    if site.endswith(file_types[0]):

        new_dir(file_types[0])
        new_path = os.path.isfile(
            shutil.move(f"{path_main}/{each_file}", file_types[0])
        )

    else:
        print("erro")
