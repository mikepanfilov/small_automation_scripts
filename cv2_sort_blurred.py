#
# Sorts pictures in current directory into two subdirs, blurred and ok
#

import os
import shutil
import cv2

PROCESS_DIR = '/Volumes/SEGT/Yandex.Foto/jpg_files'
SEARCH_EXT = '.JPG'
FOCUS_THRESHOLD = 80
BLURRED_DIR = PROCESS_DIR+'/blurred'
OK_DIR = PROCESS_DIR+'/ok'

blur_count = 0
ok_count = 0
missed_count = 0
files = []
for f in os.listdir(PROCESS_DIR):
   if f.endswith(SEARCH_EXT):
      files.append(PROCESS_DIR+'/'+f)

try:
   os.makedirs(BLURRED_DIR)
   os.makedirs(OK_DIR)
except:
   pass

for infile in files:

   print('-'*150)
   print('Processing file %s ...' % (infile))
   print('-'*150)

   try:
      cv_image = cv2.imread(infile)

      # Covert to grayscale
      gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

      # Compute the Laplacian of the image and then the focus
      #     measure is simply the variance of the Laplacian
      variance_of_laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()

      # If below threshold, it's blurry
      if variance_of_laplacian < FOCUS_THRESHOLD:
         shutil.move(infile, BLURRED_DIR)
         blur_count += 1
      else:
         shutil.move(infile, OK_DIR)
         ok_count += 1
   except:
      missed_count += 1
      print(infile,'cant process')

print('Done.  Processed %d files: \n%d - missed\n%d blurred\n%d ok.' % (len(files), missed_count, blur_count, ok_count))