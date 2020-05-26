from zipfile import ZipFile
from os import listdir

PATH = '/Users/panfilovlar/Downloads/Chemistry/'

for d in listdir(PATH):
    if d not in (['.DS_Store', 'python_zipper.py']):
        print('----', d, '----')
        zip = ZipFile(PATH + '/' + d + '.zip', 'w')
        for f in listdir(PATH + '/' + d):
            zip.write(PATH + '/' + d + '/' + f, f)
        zip.close()