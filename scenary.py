import random
from colorama import init, Fore
init()

class Scenary:
    
    def __init__(self):
        self.__sky = Fore.BLUE+ "X" + '\x1b[0m'
        self.__ground = Fore.GREEN  + "T" + '\x1b[0m'
        self.__beams_vertical = [('++'),('++'),('++'),('++'),] 
        self.__beams_horizontal = [('++++++'),('++++++')]
        self.__beams_slant = [('++'),('++'),('++'),('++')]
        self.__dragon=[]
        self.__yoda=[]
        self.drx=0
        self.dry=0
        self.dragon_width=43
        self.dragon_height=12
        self.yoda_width=24
        self.yoda_height=6

    def create_ground(self, grid):
        for i in range(500):
            grid[29][i]=self.__ground
            grid[28][i]=Fore.LIGHTGREEN_EX+ "*" + '\x1b[0m'

    def create_sky(self, grid):
        for i in range(500):
            grid[0][i]=self.__sky

    def create_beams_vertical(self,grid,c,d):
        while(d<450):
            e=d
            f=c
            for i in range(len(self.__beams_vertical)):
                for j in range(len(self.__beams_vertical[i])):
                    grid[c][d]=Fore.RED + self.__beams_vertical[i][j] + '\x1b[0m'
                    d+= len(self.__beams_vertical[i][j])
                d=e
                c+=1
            if(f+6<24):
                c=f+6
            else:
                c=3   
            d+=70 

    def create_beams_horizontal(self,grid,c,d):
        while(d<450):
            e=d
            f=c
            for i in range(len(self.__beams_horizontal)):
                for j in range(len(self.__beams_horizontal[i])):
                    grid[c][d]=Fore.RED +self.__beams_horizontal[i][j]+ '\x1b[0m'
                    d+= len(self.__beams_horizontal[i][j])
                d=e
                c+=1
            if(f+6<24):
                c=f+6
            else:
                c=6
            d+=50


    def create_beams_slant(self,grid,c,d):
        while(d<450):
            e=d
            f=c
            for i in range(len(self.__beams_slant)):
                for j in range(len(self.__beams_slant[i])):
                    grid[c][d]=Fore.RED +self.__beams_slant[i][j]+ '\x1b[0m'
                    d+=len(self.__beams_slant[i][j])
                e+=1
                d=e
                c+=1
            c=f
            d+=70  
                               

    def create_coins(self,grid,tempx,tempy):
        for i in range(2):
            i=i
            for k in range(3):
                tempy+=1
                for j in range(8):
                    if(grid[tempx+k][tempy+j]==' '):
                        grid[tempx+k][tempy+j]=Fore.YELLOW+ "$" + '\x1b[0m'

    def create_speedup(self,grid,tempx,tempy):
        if(grid[tempx][tempy]==' '):
            grid[tempx][tempy]='S'

    def create_dragon(self,grid,c,d):
        with open("./dragon.txt") as obj:
            for line in obj:
                self.__dragon.append(line.strip('\n'))
        e=d
        for i in range(self.dragon_height):
            for j in range(self.dragon_width):
                grid[c][d]=self.__dragon[i][j]
                d+=1
            d=e
            c+=1
    
    def clear_dragon(self,grid,c,d):
        for i in range(c,c+self.dragon_height+2):
            for j in range(d,d+self.dragon_width):
                grid[i][j]=' '

    def create_yoda(self,grid,c,d):
        with open("./yodha.txt") as obj:
            for line in obj:
                self.__yoda.append(line.strip('\n'))
        e=d
        for i in range(self.yoda_height):
            for j in range(self.yoda_width):
                grid[c][d]=self.__yoda[i][j]
                d+=1
            d=e
            c+=1    