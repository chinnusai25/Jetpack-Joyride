import os
import time
from colorama import init,Fore
init()

class Extra_stuff:
    
    def __init__(self):
        self.__remainingtime=200
        self.__is_it_space=0
        self.__space_button_start_time=115
        self.__speedup=0
        self.__speedup_start_time=0
        self.__no_of_bullets=0
        self.__bullets_x=[]
        self.__no_of_iceballs=0
        self.__iceballs_x=[]
        self.__iceballs_move_time=0
        self.__magnet_position=0
        self.__shield_threshold_time=10
        self.__beam_atom=Fore.RED+ "+" + '\x1b[0m'
        self.__dragon_border=[",","`",":","\\","(","'","{","V","j",";","."]
        self.__dragon_lives_left=8
        self.__starting_time_of_dragon=70
        self.__extra_score=0
        self.__is_o_pressed=0

    def set_o_pressed(self):
        self.__is_o_pressed=1

    def get_o_pressed(self):
        return self.__is_o_pressed

    def unset_o_pressed(self):
        self.__is_o_pressed=0

    def remaining_time(self):
        return self.__remainingtime

    def dragon_start(self):
        return self.__starting_time_of_dragon

    def get_dragon_lives_left(self):
        return self.__dragon_lives_left

    def get_shield_threshold_time(self):
        return self.__shield_threshold_time

    def setspace(self):
        self.__is_it_space=1

    def unsetspace(self):
        self.__is_it_space=0

    def spacevalue(self): 
        return self.__is_it_space 

    def set_space_button_start_time(self,val):
        self.__space_button_start_time=val

    def get_space_button_start_time(self):
        return self.__space_button_start_time

    def setspeedup(self):
        self.__speedup=1

    def unsetspeedup(self):
        self.__speedup=0
        
    def getspeedup(self):
        return self.__speedup    

    def set_speedup_start_time(self,val):
        self.__speedup_start_time=val

    def get_speedup_start_time(self):
        return self.__speedup_start_time

    def create_bullet(self,grid,x,y):
        grid[x][y]='='

    def create_iceballs(self,grid,x,y):
        grid[x][y]='<'

    def beams_disappear(self,grid,x,y):
        j=x
        k=y
        if(grid[j][k+1]==self.__beam_atom and grid[j][k+2]==self.__beam_atom):
                    
            if(grid[j][k+3]==self.__beam_atom):         #horizontal beam
                if(grid[j-1][k+1]==self.__beam_atom):
                    for m in range (j-1,j+1):
                        for n in range(k+1,k+7):
                            if(grid[m][n]==self.__beam_atom):
                                grid[m][n]=' '

                elif(grid[j+1][k+1]==self.__beam_atom):
                    for m in range (j,j+2):
                        for n in range(k+1,k+7):
                            if(grid[m][n]==self.__beam_atom):
                                grid[m][n]=' '
                    
            elif((grid[j-1][k+1]==self.__beam_atom and grid[j-1][k+2]==self.__beam_atom) or (grid[j+1][k+1]==self.__beam_atom and grid[j+1][k+2]==self.__beam_atom) ):        #vertical beam  
                for m in range(j-3,j+4):
                    for n in range(k+1,k+3):
                        if(grid[m][n]==self.__beam_atom):
                            grid[m][n]=' '

            elif(grid[j-1][k]==self.__beam_atom or grid[j+1][k+2]==self.__beam_atom):       #slant beam
                if(grid[j-1][k]==self.__beam_atom and grid[j+1][k+2]==self.__beam_atom):
                    for m in range(j-2,j+3):
                        for n in range(k-2,k+5):
                            if(grid[m][n]==self.__beam_atom):
                                grid[m][n]=' '

                elif(grid[j-1][k]==self.__beam_atom):
                    for m in range(j-3,j+1):
                        for n in range(k-2,k+3):
                            if(grid[m][n]==self.__beam_atom):
                                grid[m][n]=' '

                else:
                    for m in range(j,j+4):
                        for n in range(k+1,k+6):
                            if(grid[m][n]==self.__beam_atom):
                                grid[m][n]=' '

    def get_extra_score(self):
        return self.__extra_score 

    def move_bullets(self,grid,x):
        j=x
        for i in range(0,110,1):        #movement of bullet
            if(grid[j][i+1]=='=' or grid[j][i]=='='):
                if(grid[j][i]=='='):
                    k=i
                elif(grid[j][i+1]=='='):
                    k=i+1
                if(grid[j][k+1]==self.__beam_atom and grid[j][k+2]==self.__beam_atom):
                
                    self.beams_disappear(grid,j,k)
                    self.__extra_score+=4
                    grid[j][k]=' '
        
                elif(grid[j][k+1] in self.__dragon_border or grid[j][k+2] in self.__dragon_border  ):
                    self.__dragon_lives_left-=1
                    self.__extra_score+=5
                    grid[j][k]=' '

                elif(grid[j][k+1]==Fore.LIGHTMAGENTA_EX + ":" + '\x1b[0m'):
                    for l in range(j,j+2):
                        for t in range(k+1,k+3):
                            grid[l][t]=' '
                    self.__extra_score+=3
                    grid[j][k]=' '
                else:    
                    grid[j][k+1]=grid[j][k]
                    grid[j][k]=' '
                break 

    def move_bullets_try(self,grid,x,k):
        j=x
        i=k
        for i in range(k,110,1):        #movement of bullet
            if(grid[j][i+1]=='=' or grid[j][i]=='='):
                if(grid[j][i]=='='):
                    grid[j][i+1]=grid[j][i]
                    grid[j][i]=' '
                elif(grid[j][i+1]=='='):
                    grid[j][i+2]=grid[j][i+1]
                    grid[j][i+1]=' '
                break

    def move_iceballs(self,grid,x):
        j=x
        k=0
        for i in range(0,110,1):        #movement of iceballs
            if(grid[j][i]=='<'):
                if(grid[j][i-1]==Fore.LIGHTCYAN_EX + ">" + '\x1b[0m' or grid[j][i-1]==Fore.LIGHTCYAN_EX + "@" + '\x1b[0m' or grid[j][i-1]==Fore.LIGHTCYAN_EX + "\\" + '\x1b[0m' ):
                    k=1
                    grid[j][i]=' '
                if(k!=1):
                    if(grid[j][i-1]=='='):
                        grid[j][i]=' '
                        grid[j][i-1]=' '
                    else:
                        grid[j][i-1]=grid[j][i]
                        grid[j][i]=' '
        return k

    def set_no_of_bullets(self):
        self.__no_of_bullets+=1
    
    def get_no_of_bullets(self):
        return self.__no_of_bullets

    def add_xcoo_of_bullets(self,x):
        self.__bullets_x.append(x)

    def get_xcoo_of_bullets(self):
        return self.__bullets_x

    
    def set_no_of_iceballs(self):
        self.__no_of_iceballs+=1
    
    def get_no_of_iceballs(self):
        return self.__no_of_iceballs

    def add_xcoo_of_iceballs(self,x):
        self.__iceballs_x.append(x)

    def get_xcoo_of_iceballs(self):
        return self.__iceballs_x

    def create_magnet(self,grid,x,y):
        if(grid[x][y]==' '):
            grid[x][y]='M'
            self.__magnet_position=y

    def get_magnet_pos(self):
        return self.__magnet_position

    def set_magnet_pos(self):
        self.__magnet_position-=1