import os
import shutil
from tkinter.filedialog import askdirectory

path = askdirectory(
    initialdir='~/downloads',
    title='Pasta destino')
names = os.listdir(path)

folder_names = ['site', 'voxus']

for x in range(0, 2):
    if not os.path.exists(path+folder_names[x]):
        os.makedirs(path+folder_names[x])
for files in names:
    if 'site' in files and not os.path.exists(path+'site/' + files):
        shutil.move(path+files, path + 'site/' + files)
    if 'voxus' in files and not os.path.exists(path + 'voxus/' + files):
        shutil.move(path+files, path + 'voxus/' + files)
