

import os
import time 

fName = 'test.txt'

fPath = '/users/danielalvarez/documents/Github/TTA-Python-Projects/scriptCheckAssignment'



""" abPath = os.path.join(fPath,fName)

print(abPath) """

dir_list = os.listdir(fPath)

''' print('Files and directories in \'', fPath, '\' :') '''

print(dir_list)

''' modTime = os.path.getmtime(abPath)

print(modTime)

print('
 '''
