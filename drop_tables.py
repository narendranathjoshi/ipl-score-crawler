'''
This file is for testing pruposes only

Not to be included in the main project deliverable
'''
from database import *

cur.execute('USE test')
cur.execute('DROP TABLE root')
for i in range(1, 77):
        dropBatQuery = 'DROP TABLE ' + str(i) + 'BA'
        dropBowlQuery = 'DROP TABLE ' + str(i) + 'BO'
        cur.execute(dropBatQuery)
        cur.execute(dropBowlQuery)
con.commit()
print('Done dropping')