import urllib.request
response = urllib.request.urlopen('http://www.iplt20league.com/ipl_6/rcb_vs_mi_scorecard_match_2.html')
html = response.read()
f = open('test.html', 'w')
print(html, file=f)
print("Done")