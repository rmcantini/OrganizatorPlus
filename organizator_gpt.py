""" Super file organizer by part of the filename """
import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory
from typing import List

# hide root window
root = tk.Tk()
root.withdraw()


def organize_files(path_main: str, file_types: List[str]):
    """Organize files by part of the filename"""
    names = os.listdir(path_main)

    # main loop
    for i in file_types:
        if not os.path.exists(os.path.join(path_main, i)):
            os.makedirs(os.path.join(path_main, i))

        for file in names:
            if i in file:
                shutil.move(os.path.join(path_main, file), os.path.join(path_main, i))

    # move remaining files to the 'social' folder
    for resto in names:
        if os.path.isfile(os.path.join(path_main, resto)):
            shutil.move(
                os.path.join(path_main, resto), os.path.join(path_main, file_types[-1])
            )


if __name__ == "__main__":
    # intro explanation pop-up
    tk.messagebox.showinfo("info", "Selecione a pasta com os desdobramentos.")

    # asks what directory to work with
    path_main = askdirectory(
        initialdir="~/downloads", title="Selecione a pasta onde estão os arquivos"
    )

    file_types = ["site", "voxus", "GDN", "social", "vtex"]
    organize_files(path_main, file_types)


"""
Changes made:

    Encapsulated the code into a function and removed unnecessary global variables.
    Replaced string concatenation with os.path.join() for creating folder paths.
    Simplified the if-else block to create folders using os.makedirs().
    Refactored the code that moves files to a target folder by using shutil.move() and os.path.join().
    Removed the redundant os.path.isfile() check before calling shutil.move().
"""
