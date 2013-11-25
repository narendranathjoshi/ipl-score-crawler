import urllib.request as request
from match_urls import matchesURL
import re
from database import *

class Implementation:    
    def __init__(self):
        #self.getFiles()    #to be uncommented
        self.getValues()
        
    def getFiles(self):  
        self.matchesResponse = []      
        for i in (range(len(matchesURL))):  # range(len(matchesURL))
            # print('a', i) #testing #success
            self.matchesResponse.append(request.urlopen(matchesURL[i]))
            a = self.matchesResponse[i].read()
            f = open('match' + str(i + 1) + '.html', 'w')
            print(a, file=f)     
            
    def getValues(self):
        create()
        for i in range(len(matchesURL)):
            if i == 71:
                continue
            filePtr = open('match' + str(i + 1) + '.html')
            text = filePtr.read()
            start = text.find('IPL Season 6 - Match')
            end = text.find('Umpires')
            text = text[start:end]
            text = re.sub('&amp;', '&', text)
            #text = re.sub('\n', '', text)
            textList = re.findall('>.*?<', text)
            usableTextList = []
            for j in range(len(textList)):
                if '><'in textList[j] or '>\\r\\n' in textList[j] or '>&nbsp;<' in textList[j] or '>\\n<' in textList[j]:
                    pass
                else:
                    usableTextList.append(textList[j][1:-1])
            d = open('usableTL'+ str(i+1) + '.txt', 'w') #test file
            for k in usableTextList:
                print(k, file = d)
            #print("Done", i + 1) #testing
            insert(i + 1, usableTextList)
    
# print("done") #testing #success
