import shutil
import os
import time
from datetime import datetime 

#set where the source of the files are
source = '/Users/danielalvarez/Documents/GitHub/TTA-Python-Projects/Challenges/fileTransfer/CreateOrMod/'

#set the destination path to folderB
destination = '/Users/danielalvarez/Documents/GitHub/TTA-Python-Projects/Challenges/fileTransfer/Receive/'
files = os.listdir(source)

now = datetime.now()
currentHour = now.strftime('%I')
currentDay = now.strftime('%d')
currentMonth = now.strftime('%m')
currentYear = now.strftime('%Y')


for i in files:
    modTime = (time.ctime(os.path.getmtime(source+i)))
    modTimeObj = datetime.strptime(modTime, '%a %b %d %H:%M:%S %Y')
    modTimeHour = modTimeObj.strftime("%I")
    modTimeDay = modTimeObj.strftime("%d")
    modTimeMonth = modTimeObj.strftime("%m")
    modTimeYear = modTimeObj.strftime("%Y")

    if currentYear == modTimeYear and currentMonth == modTimeMonth and currentDay == modTimeDay and currentHour and modTimeHour:
        print(i + ' was modified this year, this month, today, at ' + modTimeHour + ' O\'clock.')


    
'''

if 
    for i in files:
        #we are saying move the files represented by 'i' to their new destinatio
        shutil.move(source+i,destination)
'''
