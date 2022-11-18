
class Board:
    
    def __init__(self,row,column):
        self.row=row
        self.column=column
        self.matrix=[]

    def createboard(self):
        for i in range (self.row):
            i=i
            self.new=[]
            for j in range(self.column):
                j=j
                self.new.append(" ")
            self.matrix.append(self.new)

    def print(self):
        for i in range(self.row):
            for j in range(0,110):
                print(self.matrix[i][j],end='')
            print()                
        