import pymysql
import re

con = pymysql.connect()
cur = con.cursor()

def create():
    useQuery = 'USE test'
    createRootQuery = 'CREATE TABLE root (matchId INTEGER, venue CHAR(20), result CHAR(100), mom CHAR(50), score1 CHAR(40), score2 CHAR(40), PRIMARY KEY (matchId))'
    cur.execute(useQuery)
    cur.execute(createRootQuery)
    for i in range(1, 77):
        createBatQuery = 'CREATE TABLE ' + str(i) + 'BA' + '(teamID INTEGER, name CHAR(50), runs INTEGER, balls INTEGER, 4s INTEGER, 6s INTEGER)'
        createBowlQuery = 'CREATE TABLE ' + str(i) + 'BO' + '(teamID INTEGER, name CHAR(50), overs INTEGER, maidens INTEGER, runs INTEGER, wickets INTEGER)'
        cur.execute(createBatQuery)
        cur.execute(createBowlQuery)
    con.commit()

def insert(m, x):
        
    print('no' + str(m))    
    def getVenue():
        venue = ''
        for i in x:
            if 'Venue:' in i:
                venue = i
                break
        comma = venue.find(', ')
        venue = venue[comma + 2:]
        return venue
    
    def getResult():
        result = ''
        for i in x:
            title = 'Result : '
            if title in i:
                titleIndex = i.find(title)
                result = i[titleIndex + len(title):]
                break
        return result
    
    def getMom():
        mom = ''            
        for i in x:
            title = 'Man of the Match : '
            if title in i:
                titleIndex = i.find(title)
                mom = i[titleIndex + len(title):]
                break
        return mom

    def getScore():
        score1 = ''
        score2 = ''
        for i in range(len(x)):
            title = 'Total Score'
            if title in x[i]:
                if score1 == '':
                    score1 = x[i + 1] + x[i + 2]
                else:
                    score2 = x[i + 1] + x[i + 2]
        return score1 + '\', \'' + score2                                                
    
    def insertRoot():
        insertRootQuery = 'INSERT INTO root VALUES (' + str(m) + ', \'' + getVenue() + '\', \'' + getResult() + '\', \''\
         + getMom() + '\', \'' + getScore() + '\')'
        #print(insertRootQuery)
        cur.execute(insertRootQuery)
        con.commit()
        #print("done inserting root", m)
        
    def insertBat():
        index = 0
        start = [i for i,j in enumerate(x) if 'SR' == j]
        end = [i for i,j in enumerate(x) if 'Extras' in j]
        if len(start) != 0 and len(end) != 0:
            bat = x[start[0] + 1:end[0]]
            if 'Did not bat' in bat[-1]:
                flag = True
                while flag:
                    bat = bat[:-2]
                    if 'Did not bat' in bat[-1] or 'Did not Bat' in bat[-1] or 'Did not bat' in bat[-2] or 'Did not Bat' in bat[-2]:
                        flag = True
                    else:
                        flag= False
            if len(bat) % 7 != 0:
                bat = bat[:int(len(bat)/2)]
                while len(bat) % 7 != 0:
                    bat = bat[:-1]
            teamID = 1
            for i in range(0, len(bat), 7):
                name = bat[i]
                runs = bat[i+2]
                balls = bat[i+3]
                fours = bat[i+4]
                sixes = bat[i+5]
                cur.execute('INSERT INTO ' + str(m) + 'BA VALUES (' + str(teamID)+ ',\'' + name + '\', ' + str(runs) + ', ' + str(balls) + ', ' + str(fours) + ',' + str(sixes) + ')')
                con.commit()
                print('committed ', m)
                
        if len(start) > 1 and len(end) > 1:
            bat = x[start[1] + 1:end[1]]
            if 'Did not bat' in bat[-1]:
                flag = True
                while flag:
                    bat = bat[:-2]
                    if 'Did not bat' in bat[-1] or 'Did not Bat' in bat[-1] or 'Did not bat' in bat[-2] or 'Did not Bat' in bat[-2]:
                        flag = True
                    else:
                        flag= False
            if len(bat) % 7 != 0:
                bat = bat[:int(len(bat)/2)]
                while len(bat) % 7 != 0:
                    bat = bat[:-1]
            teamID = 2
            for i in range(0, len(bat), 7):
                name = bat[i]
                runs = bat[i+2]
                balls = bat[i+3]
                fours = bat[i+4]
                sixes = bat[i+5]
                cur.execute('INSERT INTO ' + str(m) + 'BA VALUES (' + str(teamID)+ ',\'' + name + '\', ' + str(runs) + ', ' + str(balls) + ', ' + str(fours) + ',' + str(sixes) + ')')
                con.commit()
                print('committed ', m)
            
    def insertBowl():
        index = 0
        start = [i for i,j in enumerate(x) if 'WD' == j]
        end = [i for i,j in enumerate(x) if '2nd Innings' in j]
        #print(m, start, end, len(x))
        if len(start) != 0 and len(end) != 0:
            bowl = x[start[0] + 1:end[0]]
            #print(bowl)
        
        
    
    insertRoot()
    insertBat()
    insertBowl()