import os
import shutil

from datetime import date
from datetime import time
from datetime import datetime

from os import path
from shutil import make_archive
from zipfile import ZipFile



#set file name and time of creation
today = datetime.now()
fileName = 'zipper_' + today.strftime('%Y.%m.%dh%H%M') + '.zip'
dirName = 'tmp/'
# add path to directory

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = ZipFile(fileName, 'w')
    zipdir(dirName, zipf)
    zipf.close()

