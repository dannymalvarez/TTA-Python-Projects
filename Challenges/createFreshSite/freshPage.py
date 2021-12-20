
import webbrowser as w
import os


go = 'newPage.html'
place = '/Users/danielalvarez/Documents/GitHub/TTA-Python-Projects/Challenges/createFreshSite/'

placeCheck = os.listdir(place)
abPath = os.path.join(place,go)
final = 'file://' + abPath
print(final)

if go in placeCheck:
    f = open('newPage.html','r')
    f.close()
    w.get('chrome').open(final)
    
else:
    f = open('newPage.html','w')
    f.write('<html><body><h1>Stay tuned for our amazing summer sale!</h1></body></html>')
    f.close()
    w.get('chrome').open(final)






