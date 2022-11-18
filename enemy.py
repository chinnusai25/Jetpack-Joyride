from person import Person
from colorama import Fore,init
init()

class Enemy(Person):

    def shape(self):
        self._shape=[":",":",";",";"]

    def start(self,grid):
        temp=-1
        for i in range(self._x,self._x+2,1):    
            for j in range(self._y,self._y+2,1):    
                temp+=1
                grid[i][j]=Fore.LIGHTMAGENTA_EX + self._shape[temp] + '\x1b[0m'

    