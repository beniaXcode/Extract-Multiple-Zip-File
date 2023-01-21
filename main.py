import os
from zipfile import ZipFile
dir_path= "the path to directory contain zip files"

def get_fils(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)):
            yield file


# loading the temp.zip and creating a zip object
for file in get_fils(dir_path):
    with ZipFile(os.path.join(dir_path,file), 'r') as zObject:
        zObject.extractall(path="path to directory where the extracted files will go to")