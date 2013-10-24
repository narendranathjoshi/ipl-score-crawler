import urllib.request

"""
match1= urllib.request.urlopen('http://www.iplt20league.com/ipl_6/kkr_vs_dd_scorecard_match_1.html')
match2= urllib.request.urlopen('http://www.iplt20league.com/ipl_6/rcb_vs_mi_scorecard_match_2.html')
match3= urllib.request.urlopen('http://www.iplt20league.com/ipl_6/srh_vs_pwi_scorecard_match_3.html')
"""

listmatches=[match1,match2,match3]


for i in range(len(listmatches)):
    ht=listmatches[i].read()
    f=open('match'+str(i)+'.html','w')
    print(ht,file=f)
    
print("done")



