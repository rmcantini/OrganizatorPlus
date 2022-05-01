''' Super file organizer by part of the filename '''
import os
import shutil
import tkinter
from tkinter.filedialog import askdirectory

# asks what directory to work with
path = askdirectory(
    initialdir='~/downloads',
    title='Selecione a pasta onde estão os arquivos')
names = os.listdir(path)

# criar subpastas destino
try:
    if not os.path.exists(path):
        os.makedirs(path)

    # Creates the subfolders
    os.chdir(path)
    NEWFOLDER_1 = 'site'
    os.makedirs(NEWFOLDER_1)
    NEWFOLDER_2 = 'voxus'
    os.makedirs(NEWFOLDER_2)
    NEWFOLDER_3 = 'social'
    os.makedirs(NEWFOLDER_3)

    # Success feedback
    tkinter.messagebox.showinfo('info', 'Sucesso Total!')

# Error feedback
except OSError:
    tkinter.messagebox.showinfo('info', 'Erro: A pasta já existe! \
		                         Verifique o nome da task.')

# selecionar os arquivos que contenham a palavra e mover para a pasta certa
for file in names:
    if "site" in file:
        new_path = shutil.move(f"{path}/{file}", NEWFOLDER_1)

    elif "voxus" in file:
        new_path = shutil.move(f"{path}/{file}", NEWFOLDER_2)
    else:
        new_path = shutil.move(f"{path}/{file}", NEWFOLDER_3)
