

import os
import time 


fName2 = 'test2.txt'
fName = 'test.txt'

fPath = '/users/danielalvarez/documents/Github/TTA-Python-Projects/scriptCheckAssignment'


abPath = os.path.join(fPath,fName)
abPath2 = os.path.join(fPath,fName2)

print(abPath)
print('\n')
print(abPath2)
print('\n')

dir_list = os.listdir(fPath)

print(dir_list)
print('\n')


#print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
#print("Created: %s" % time.ctime(os.path.getctime("test.txt")))


modTime = (time.ctime(os.path.getmtime(abPath)))
modTime2 = (time.ctime(os.path.getmtime(abPath2)))

with open(fName,'r') as a:
    data1 = a.read()
    a.close()
print('The first file is ' + fName + ' which contains: \n' + data1 + ' \nIt was created/modified on ' + str(modTime))
print('\n')
with open(fName2,'r') as b:
    data2 = b.read()
    b.close()
print('The second file is ' + fName2 + ' which contains: \n' + data2 + ' \nIt was created/modified on ' + str(modTime2))


