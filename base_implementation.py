import urllib.request as request
from match_urls import matchesURL

class Implementation:
    
    def __init__(self):
        self.getFiles()
        #self.openFiles()
        
    def getFiles(self):  
        self.matchesResponse = []      
        for i in (range(len(matchesURL))): #range(len(matchesURL))
            #print('a', i) #testing #success
            self.matchesResponse.append(request.urlopen(matchesURL[i]))
            a = self.matchesResponse[i].read()
            f = open('match' + str(i+1) + '.html', 'w')
            print(a, file = f)                     
    
#print("done") #testing #success