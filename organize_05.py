''' Super file organizer by part of the filename '''
import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory


# hide root window
root = tk.Tk()
root.withdraw()

# intro explanation pop-up
tk.messagebox.showinfo(
    'info', 'Selecione a pasta com os desdobramentos.')

# asks what directory to work with
path_main = askdirectory(
    initialdir='~/downloads',
    title='Selecione a pasta onde estão os arquivos')
names = os.listdir(path_main)


# creates list of subfolders
if not os.path.exists(path_main):
    os.makedirs(path_main)

os.chdir(path_main)
NEWFOLDER_1 = 'site'
os.makedirs(NEWFOLDER_1)
NEWFOLDER_2 = 'voxus'
os.makedirs(NEWFOLDER_2)
NEWFOLDER_3 = 'GDN'
os.makedirs(NEWFOLDER_3)
NEWFOLDER_4 = 'social'
os.makedirs(NEWFOLDER_4)
NEWFOLDER_5 = 'vtex'
os.makedirs(NEWFOLDER_5)


try:
    # selecionar os arquivos que contenham a palavra e mover para a pasta certa
    for file in names:
        if 'site' in file:
            new_path = os.path.isfile(shutil.move(
                f"{path_main}/{file}", NEWFOLDER_1))

        elif 'voxus' in file:
            new_path = os.path.isfile(shutil.move(
                f"{path_main}/{file}", NEWFOLDER_2))

        elif 'GDN' in file:
            new_path = os.path.isfile(shutil.move(
                f"{path_main}/{file}", NEWFOLDER_3))

        elif 'vtex' in file:
            new_path = os.path.isfile(shutil.move(
                f"{path_main}/{file}", NEWFOLDER_5))

        elif 'dark' in file:
            new_path = os.path.isfile(shutil.move(
                f"{path_main}/{file}", NEWFOLDER_4))

        elif 'stories' in file:
            new_path = os.path.isfile(shutil.move(
                f"{path_main}/{file}", NEWFOLDER_4))

        elif 'miner' in file:
            new_path = os.path.isfile(shutil.move(
                f"{path_main}/{file}", NEWFOLDER_4))

        else:
            pass

    for item in os.listdir(path_main):
        if os.path.isdir(item):
            if not os.listdir(item):
                os.removedirs(os.path.join(path_main, item))

    # showinfo('info', 'Sucesso Total!')Success feedback
    tk.messagebox.showinfo('info', 'Sucesso Total!')

except OSError:
    tk.messagebox.showinfo(
        'info', 'Ocorreu algum problema, verifique se a pasta de arquivos é a correta.')
