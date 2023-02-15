import os
import shutil

# path of the directory where the files are located
path = "/Users/Desktop/files"

# move python files into their own subfolder
files = os.listdir(path)

# iterate over the files
for file in files:
    if file.endswith(".py"):
        os.makedirs(os.path.join(path, "python_files"))
        shutil.move(os.path.join(path, file), os.path.join(path, "python_files"))

# move txt files into their own subfolder
files = os.listdir(path)

for file in files:
    if file.endswith(".txt"):
        os.makedirs(os.path.join(path, "text_files"))
        shutil.move(os.path.join(path, file), os.path.join(path, "text_files"))


'''


def move_files(files, path, extension):
    for file in files:
        if file.endswith(extension):
            os.makedirs(os.path.join(path, "extension_files"))
            shutil.move(os.path.join(path, file), os.path.join(path, "extension_files"))




def create_folders(words, folder):
  for word in words:
    for file in folder:
      if word in file.name:
        new_folder = folder.create_folder(word)
        new_folder.move(file)

# usage example
words = ['dogs', 'cats']
folder = '/home/my_folder'
create_folders(words, folder)


```

