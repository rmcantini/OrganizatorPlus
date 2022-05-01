''' Super file organizer by part of the filename '''
import glob
import os
from tkinter.filedialog import askdirectory

# gets the names in directory
#file_list = os.listdir("~/Downloads/files")
file_list = askdirectory(
    initialdir='~/downloads',
    title='Pasta destino')


def type_file(x):
    '''grab last 4 characters of the file name'''
    return(x[-4:])


sorted(file_list, key=type_file)

# read in and process them in sorted order
for filename in sorted(file_list, key=type_file):
    with open(filename, 'rb') as thefile:
        # Do stuff to each file
        for f in glob.glob('*.png'):
            cwd = os.getcwd()
            dir_name = cwd+'//'+type_file(f)
            print(dir_name)
            if not os.path.exists(dir_name):
                os.mkdir(dir_name)
            os.rename(f, dir_name+'//'+f)
