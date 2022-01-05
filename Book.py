from datetime import date

class Book: 
    def __init__(self, title, pagesRead, totalPages, completed, dateCompleted):
        self.title = title
        self.pagesRead = pagesRead
        self.totalPages = totalPages
        if str(completed) == 'False':
            self.completed = False
        else: 
            self.completed = True
        self.dateCompleted = dateCompleted

    #getters
    def getTitle(self): 
        return self.title
        
    def getPagesRead(self):
        return self.pagesRead

    def getTotalPages(self):
        return self.totalPages
    
    def getCompleted(self):
        return self.completed

    def getDateCompleted(self):
            return self.dateCompleted
    
    #setters
    def updatePagesRead(self, pageNumber):
        if pageNumber >= self.totalPages:
            self.isCompleted()
            self.pagesRead = self.totalPages
        else:
            self.pagesRead = pageNumber

        if(pageNumber == self.totalPages):
            self.isCompleted()
    
    def isCompleted(self):
        if self.completed != True:
            self.completed = True
            self.setDateCompleted()
    
    def setDateCompleted(self): 
        self.dateCompleted = date.today().strftime("%m/%d/%Y")

    #functions
    def percentCompleted(self): 
        return round(100 *(self.pagesRead/self.totalPages), 1)

