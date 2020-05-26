from os import walk, rename
from os.path import relpath, join

PATH = '/Users/panfilovlar/Documents/GitHub'
IGNORE = ('.DS_Store')

for path,subfolder,files in walk(PATH):
    if path not in IGNORE: 
        for f in files:
            if f not in IGNORE:
                print(path)
                print(subfolder)