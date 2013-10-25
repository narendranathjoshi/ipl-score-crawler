import urllib.request
from match_urls import listmatches


#listmatches=[match1,match2,match3]


for i in range(len(listmatches)):
    ht=listmatches[i].read()
    f=open('match'+str(i)+'.html','w')
    print(ht, file = f)
    
print("done")



