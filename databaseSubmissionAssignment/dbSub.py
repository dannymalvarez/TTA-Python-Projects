import sqlite3
import os

path = '/users/danielalvarez/documents/Github/TTA-Python-Projects/databaseSubmissionAssignment'
finPath = os.listdir(path)

info = ()
infoList = list(info)
for name in finPath:
    if name.endswith('.txt'):
        infoList.append(name)
info = tuple(infoList)


conn = sqlite3.connect('dbSub.db')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_info(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_info TEXT)')
    conn.commit()

conn = sqlite3.connect('dbSub.db')

for x in info:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO tbl_info (col_info) VALUES(?)', (x,))
            print(x)
            
       
conn.close()


file1 = info[0]
file2 = info[1]

with open(file1,'r') as a:
    output1 = a.read()
    a.close()
print(output1)
with open(file2,'r') as b:
    output2 = b.read()
    b.close()
print(output2)

