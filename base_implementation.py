import urllib.request as request
from match_urls import matchesURL
import re
from database import *

match_names = []
class Implementation:    
    def __init__(self, frame):
        self.frame = frame
        #self.getFiles()    #to be uncommented
        self.getValues()
        
    def getFiles(self):  
        self.matchesResponse = []      
        for i in (range(len(matchesURL))):  # range(len(matchesURL))
            self.frame.initProgressLabel("Crawling Match " + (i+1))
            # print('a', i) #testing #success
            self.matchesResponse.append(request.urlopen(matchesURL[i]))
            a = self.matchesResponse[i].read()
            f = open('match' + str(i + 1) + '.html', 'w')
            print(a, file=f)     
            
    def getValues(self):
        create()
        for i in range(len(matchesURL)):
            self.frame.initProgressLabel("Crawled and Updated Database")
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
                if '><'in textList[j] or '>\\r\\n' in textList[j] or '>&nbsp;<' in textList[j] or '>\\n<' in textList[j] or '>\\n\\n<' in textList[j]:
                    pass
                else:
                    usableTextList.append(textList[j][1:-1])
            d = open('usableTL'+ str(i+1) + '.txt', 'w') #test file
            for k in usableTextList:
                print(k, file = d)
            #print("Done", i + 1) #testing
            match_names.append('Match ' + str(i+1) + ' : ' + usableTextList[0])
            insert(i + 1, usableTextList)
            
    def performQuery(self, matchID, checkList):
        returnResult = []
        queryDictionary1 = {0: 'SELECT MAX(runs) FROM ' + matchID + 'BA', 1: 'SELECT MAX(wickets) FROM ' + matchID + 'BO', \
                           2: 'SELECT MAX(6s) FROM ' + matchID + 'BA', 3: 'SELECT MAX(4s) FROM ' + matchID + 'BA', \
                           4: 'SELECT MAX(overs) FROM ' + matchID + 'BO', 5: 'SELECT MAX(maidens) FROM ' + matchID + 'BO', \
                           6: 'SELECT MIN(runs/overs) FROM ' + matchID + 'BO', 7: 'SELECT result, score1, score2 FROM root WHERE matchId = ' + matchID, \
                           8: 'SELECT result, score1, score2 FROM root WHERE matchId = 76', 9: 'SELECT MAX(runs) FROM ' + matchID + 'BA'}
        for k in checkList:
            if k != 7 and k != 8:
                res1 = query(queryDictionary1.get(k))
                val = None
                for row in res1:
                    val = row[0]
                queryDictionary2 = {0: 'SELECT name FROM ' + str(matchID) + 'BA WHERE runs = ' + str(val), \
                           1: 'SELECT name FROM ' + str(matchID) + 'BO WHERE wickets = ' + str(val), \
                           2: 'SELECT name FROM ' + str(matchID) + 'BA WHERE 6s = ' + str(val), \
                           3: 'SELECT name FROM ' + str(matchID) + 'BA WHERE 4s = ' + str(val), \
                           4: 'SELECT name FROM ' + str(matchID) + 'BO WHERE overs = ' + str(val), \
                           5: 'SELECT name FROM ' + str(matchID) + 'BO WHERE maidens = ' + str(val), \
                           6: 'SELECT name FROM ' + str(matchID) + 'BO WHERE runs/overs = ' + str(val), \
                           9: 'SELECT name FROM ' + str(matchID) + 'BA WHERE runs = ' + str(val)}
                res2 = query(queryDictionary2.get(k))
                val2 = None
                for row in res1:
                    val2 = row[0]
                resTuple = (val, val2)
                returnResult.append(resTuple)
            else:
                res1 = query(queryDictionary1.get(k))
                val = None
                for row in res1:
                    val = row
                returnResult.append(val)
        return returnResult            
    
# print("done") #testing #success