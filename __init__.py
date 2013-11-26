from base_implementation import *
from tkinter import *
from tkinter import messagebox as box
from tkinter import ttk as prog 
import match_urls

class Window(Frame):
    def __init__(self,  parent):
        Frame.__init__(self,  parent,  background = '#EED')
        self.parent  =  parent
        self.initUI()
        self.initLabels()
        self.initButtons()
        self.initRadioButtons()        
        
    def initUI(self):
        self.parent.title('IPL Score Crawler')
        self.pack(fill = BOTH,  expand = 1)
        sw  =  self.parent.winfo_screenwidth()
        sh  =  self.parent.winfo_screenheight()
        self.parent.geometry('600x600+%d+%d' % ((sw - 600)/2,  (sh - 600)/2))
        
    def initProgressLabel(self, param = "..."):
        pgLabel  =  Label(self,  text  =  param,  background  =  "#EED",  font  =  ("Helvetica", "10", "bold"))
        pgLabel.place(relx  =  "0.4",  rely  =  "0.28",  relwidth  =  "0.5")    
    
    def initLabels(self):    
        h1  =  Label(self,  text  =  "IPL SCORE CRAWLER",  background  =  "#EED",  font  =  ("Helvetica", "18", "bold"))
        h2  =  Label(self,  text  =  "A Python Mini-Project",  background  =  "#EED",  font  =  ("Helvetica", "14"))
        h1.place(relx  =  "0.15",  rely  =  "0.075",  relwidth  =  "0.7")
        h2.place(relx  =  "0.15",  rely  =  "0.15",  relwidth  =  "0.7")
        operations = Label(self,  text = "Operations to be performed:\nHighest:", background = "#EED", font = ("times", "15", "bold"))
        lowest = Label(self, text = " Lowest:", background = "#EED", font = ("times", "15", "bold"))
        result = Label(self, text = "Result:", background = "#EED", font = ("times", "15", "bold"))
        operations.place(relx = "0.05", rely = "0.55")    
        lowest.place(relx = "0.6", rely = "0.58", relwidth = "0.15")
        result.place(relx = "0.6", rely = "0.68", relwidth = "0.15")
        
    def onStart(self):
        self.impl  =  Implementation(self)
        self.initOptionsMenu()
        
    def onAbout(self):
        message = '''
        IPL SCORE CRAWLER

        Python Application Programming Mini-project
        
        Team ID – 23
                
        Narendra Nath Joshi - 1PI11CS102
        Nikitha Nagaraj - 1PI11CS109
        Prerana K - 1PI11CS123        (V Sem 'B' Section)
            
        This project aims to develop an application which crawls web pages and retrieves information regarding scores and other match details into a local database. Divided into three logical modules, the first module takes care of the crawling and retrieval of web pages into the local filesystem in the form of HTML pages. Web-based library modules like urllib is being employed. The second module handles the extraction of relevant and meaningful match data from the HTML code into the application buffer, built with appropriate data structures. Regular expressions and string processing techniques are the tools being used in the second module. The third module is concerned with pushing all data into a local database which enables users to perform queries on the same. To facilitate high efficiency in storage and query optimization, the databases will be appropriately normalized. 
        '''
        box.showinfo("About", message)
        
    def onQuery(self):
        checkList = []
        for i in range(len(self.varList)):
            if self.varList[i].get() == 1:
                checkList.append(i)
        #print(checkList)
        matchID = self.strvar.get()
        matchID = matchID[matchID.find('h ') + 2:matchID.find(':')][:-1]
        #print('aaaa' + matchID + 'aaa')
        if len(checkList) == 0:
            box.showerror("Error", "You did not select a criteria")
        else:
            a = self.impl.performQuery(matchID, checkList)
            resMsg = ''
            for d in a:
                for j in d:
                    resMsg += (str(j) + '\t')
                resMsg += '\n\n' 
            box.showinfo("Query Result", resMsg)
    
    def initButtons(self):
        startButton  =  Button(self, text = "Start", font  =  ("times", "11", "bold"), command = self.onStart, background = "#5DC8CD")
        startButton.place(relx = "0.1", rely = "0.27", relwidth = "0.25")
        quitButton = Button(self, text = "Quit", background = "#5DC8CD", font = ("times", "11", "bold"), command = self.quit)
        aboutButton = Button(self, text = "About", background = "#5DC8CD", font = ("times", "11", "bold"), command = self.onAbout)
        aboutButton.place(relx = "0.5", rely = "0.9", relwidth = "0.15")
        quitButton.place(relx = "0.7", rely = "0.9", relwidth = "0.15")
        queryButton = Button(self, text = "Query", font  =  ("times", "11", "bold"), command = self.onQuery, background = "#5DC8CD")
        queryButton.place(relx = "0.1", rely = "0.9", relwidth = "0.25")
    
    def initOptionsMenu(self):
        choose = Label(self,  text = "Choose A Match", background = "#EED", font = ("times", "16", "bold"))
        choose.place(relx = "0.05", rely = "0.4", relwidth = "0.35")
        self.strvar  =  StringVar()
        self.strvar.set('Select a match')
        #v  =  IntVar()
        self.choices  =  match_names
        self.option  =  OptionMenu(self,  self.strvar,  *self.choices)
        self.option.place(relx = "0.08", rely = "0.45", relwidth = "0.7")
        
    def initRadioButtons(self):
        self.varList = []
        for i in range(10):
            self.varList.append(IntVar())
        self.rb1 = Checkbutton(self, text = 'Runs', background = "#EED", variable = self.varList[0])
        self.rb2 = Checkbutton(self, text = 'Wickets', background = "#EED", variable = self.varList[1])
        self.rb3 = Checkbutton(self, text = 'Sixes', background = "#EED", variable = self.varList[2])
        self.rb4 = Checkbutton(self, text = 'Fours', background = "#EED", variable = self.varList[3])
        self.rb5 = Checkbutton(self, text = 'Overs Bowled', background = "#EED", variable = self.varList[4])
        self.rb6 = Checkbutton(self, text = 'Maiden Overs', background = "#EED", variable = self.varList[5])
        self.rb7 = Checkbutton(self, text = 'Economy', background = "#EED", variable = self.varList[6])
        self.rb8 = Checkbutton(self, text = 'Match', background = "#EED", variable = self.varList[7])
        self.rb9 = Checkbutton(self, text = 'Tournament', background = "#EED", variable = self.varList[8])
        self.rb10 = Checkbutton(self, text = 'Strike Rate', background = "#EED", variable = self.varList[9])
        self.rb1.place(relx = "0.05", rely = "0.65");
        self.rb2.place(relx = "0.05", rely = "0.68");
        self.rb3.place(relx = "0.05", rely = "0.71");
        self.rb4.place(relx = "0.05", rely = "0.74");
        self.rb5.place(relx = "0.05", rely = "0.77");
        self.rb6.place(relx = "0.05", rely = "0.8");
        self.rb7.place(relx = "0.62", rely = "0.62");
        self.rb8.place(relx = "0.62", rely = "0.72");
        self.rb9.place(relx = "0.62", rely = "0.75");
        self.rb10.place(relx = "0.05", rely = "0.83");   

def main():
    main  =  Tk()
    app  =  Window(main)
    main.mainloop()
    
main()