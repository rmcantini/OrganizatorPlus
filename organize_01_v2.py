''' Super file organizer by part of the filename '''
import glob
import os


file_list = os.listdir("~/downloads")


def get_dir_name(filename):
    '''gets folder name from file'''
    folder_name = filename.rfind('_site_')
    return filename[folder_name]


# iterate over files, create dirs which don't exist and move files there
for f in glob.glob('*.png'):
    cwd = os.getcwd()
    dir_name = cwd+'/'+get_dir_name(f)
    print(dir_name)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    os.rename(f, dir_name+'/'+f)
