import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory
from typing import List
import zipfile

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

    # compress folders
    zip_file_path = os.path.join(path_main, "compressed_folders.zip")
    with zipfile.ZipFile(zip_file_path, "w") as zip_file:
        for folder in file_types:
            folder_path = os.path.join(path_main, folder)
            if os.path.exists(folder_path):
                zip_file.write(folder_path, arcname=folder)
                shutil.rmtree(folder_path)

    # move compressed zip file to the 'social' folder
    shutil.move(zip_file_path, os.path.join(path_main, file_types[-1]))


if __name__ == "__main__":
    # intro explanation pop-up
    tk.messagebox.showinfo("info", "Selecione a pasta com os desdobramentos.")

    # asks what directory to work with
    path_main = askdirectory(
        initialdir="~/downloads", title="Selecione a pasta onde estão os arquivos"
    )

    file_types = ["site", "voxus", "GDN", "social", "vtex"]
    organize_files(path_main, file_types)
