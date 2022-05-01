''' Super file organizer by part of the filename '''
import glob
import os


file_list = os.listdir("~/Downloads/files")

def get_dir_name(filename):
    '''gets folder name from file'''
    pos1 = filename.rfind('_')
    pos2 = filename.find('.')
    return filename[pos1+1:pos2]


# iterate over files, create dirs which don't exist and move files there
for f in glob.glob('*.*'):
    cwd = os.getcwd()
    dir_name = cwd+'/'+get_dir_name(f)
    print(dir_name)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    os.rename(f, dir_name+'/'+f)
