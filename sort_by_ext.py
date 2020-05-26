import os
import fnmatch

MAIN_PATH = '/Volumes/SEGT/Yandex.Foto/'

# destinations
JPG_PATH = '/Volumes/SEGT/Yandex.Foto/photos_sorted'
MP4_PATH = '/Volumes/SEGT/Yandex.Foto/videos_sorted_mp4'
MOV_PATH = '/Volumes/SEGT/Yandex.Foto/videos_sorted_mov'

# photos to one path
'''
for r,d,f  in os.walk(MAIN_PATH):
    for i in fnmatch.filter(f,'*.JPG'):
        # print(r+'/'+i,'---->>', JPG_PATH+'/'+i)
        os.rename(r+'/'+i, JPG_PATH+'/'+i)
'''
# videos to one path (MP4)
'''
for r,d,f  in os.walk(MAIN_PATH):
    for i in fnmatch.filter(f,'*.MP4'):
        # print(r+'/'+i,'---->>', MP4_PATH+'/'+i)
        os.rename(r+'/'+i, MP4_PATH+'/'+i)
'''
ext_list = []
for r,d,f  in os.walk(MAIN_PATH):
    for i in f:
        if i.split('.')[1] not in ext_list:
            if i.split('.')[1] not in ('DS_Store', 'py'):
                ext_list.append(i.split('.')[1])


for ext in ext_list:
    try:
        os.mkdir(MAIN_PATH + ext + '_files')
    except OSError as error:
        print('Path', ext+ '_files', 'already exists.')

for ext in ext_list:
    for r,d,f  in os.walk(MAIN_PATH):
        for i in fnmatch.filter(f,'*.'+ext):
            # print(r+'/'+i,'---->>', MAIN_PATH+ext+'_files'+'/'+i)
            os.rename(r+'/'+i, MAIN_PATH+ext+'_files'+'/'+i)