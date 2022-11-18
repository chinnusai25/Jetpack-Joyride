import os
import time
from colorama import init,Fore
init()

class Person:
    
    def __init__(self,x,y):
        
        self._x=x
        self._y=y
        self._lives=1

    def shape(self):
        self._shape = [" ","@"," ","<",":",">","/"," ","\\"]

    def decrease_lives(self):
        self._lives-=1

    def lives_left(self):
        return self._lives

    def start(self,grid):
        temp=-1
        for i in range(25,28,1):    
            for j in range(0,3,1):    
                temp+=1
                grid[i][j]=Fore.LIGHTCYAN_EX + self._shape[temp] + '\x1b[0m'

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self,value):
        self._x=value

    def set_y(self,value):
        self._y=value