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


def main():
    """main shit"""

    # main loop
    for i in file_types:
        os.makedirs(os.path.join(path_main, i), exist_ok=True)
        for file in names:
            if i in file:
                shutil.move()
