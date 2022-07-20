""" Super file organizer by part of the filename """
import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory
from turtle import clear

from pkg_resources import cleanup_resources


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


# main loop
def check(test):

    for file in names:
        if test in file:
            print(file)

    for types in file_types:
        if test in types:
            print(types)


check("site")
