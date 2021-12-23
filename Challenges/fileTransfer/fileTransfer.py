import shutil
import os

#set where the source of the files are
source = '/Users/danielalvarez/Documents/GitHub/TTA-Python-Projects/Challenges/fileTransfer/folderA/'

#set the destination path to folderB
destination = '/Users/danielalvarez/Documents/GitHub/TTA-Python-Projects/Challenges/fileTransfer/folderB/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destinatio
        shutil.move(source+i,destination)
