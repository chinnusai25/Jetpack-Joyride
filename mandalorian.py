from scenary import *
from extra_stuff import *
from board import *
from alarmexception import *
from getch import *
from person import Person

class Mandalorian(Person):
    
    def __init__(self,x,y):

        super().__init__(x,y)
        self.__coins_collected=0
        self.__is_it_safe=0
        self.__spacevalue=0
        self.__addx=[]
        self.__addy=[]
        self.__board_present_y=0
        self._lives=5

    def set_board_present_y(self):
        self.__board_present_y+=1

    def setspace(self):
        self.__spacevalue=1

    def unsetspace(self):
        self.__spacevalue=0

    def increase_coins(self):
        self.__coins_collected+=1

    def no_of_coins_collected(self):
        return self.__coins_collected

    def safety_check_at_right_move(self,grid):
        if (grid[self._x][self._y+1]== (Fore.RED+ "+" + '\x1b[0m' ) or
            grid[self._x][self._y+2]==(Fore.RED+ "+" + '\x1b[0m'  ) or
            grid[self._x][self._y+3]==(Fore.RED+ "+" + '\x1b[0m'  ) ):

            return 1

        elif (grid[self._x+1][self._y+3]== (Fore.LIGHTMAGENTA_EX+ ":" + '\x1b[0m' )):

            return 1
            
        else:
            return 0   

    def safety_check_at_left_move(self,grid):
        if (grid[self._x][self._y-1]==(Fore.RED+ "+" + '\x1b[0m'  )):

            return 1

        elif (grid[self._x+1][self._y-1]== (Fore.LIGHTMAGENTA_EX+ ":" + '\x1b[0m' )):

            return 1
        else:
            return 0                  

    def safety_check_at_up_move(self,grid):
        if (grid[self._x-1][self._y]==(Fore.RED+ "+" + '\x1b[0m'  ) or 
            grid[self._x-1][self._y+1]==(Fore.RED+ "+" + '\x1b[0m'  ) or
            grid[self._x-1][self._y+2]==(Fore.RED+ "+" + '\x1b[0m'  ) ):
            return 1 
        else:
            return 0
    
    def safety_check_at_down_move(self,grid):
        if (grid[self._x+3][self._y]==(Fore.RED+ "+" + '\x1b[0m' or Fore.LIGHTMAGENTA_EX+ ":" + '\x1b[0m' ) or 
            grid[self._x+3][self._y+1]==(Fore.RED+ "+" + '\x1b[0m' or Fore.LIGHTMAGENTA_EX+ ":" + '\x1b[0m' ) or
            grid[self._x+3][self._y+2]==(Fore.RED+ "+" + '\x1b[0m' or Fore.LIGHTMAGENTA_EX+ ":" + '\x1b[0m' ) ):
            return 1 

        elif (grid[self._x+3][self._y]== (Fore.LIGHTMAGENTA_EX+ ":" + '\x1b[0m' )):

            return 1

        else:
            return 0
    
    def need_to_be_updated(self,grid):
        for i in range(self._x,self._x+3,1):
            for j in range(self._y,self._y+3,1):
                grid[i][j]=" "

    def is_updated(self,grid):
        temp=-1
        for i in range(self._x,self._x+3,1):    
            for j in range(self._y,self._y+3,1):    
                temp+=1
                if(self.__spacevalue==0):
                    grid[i][j]=Fore.LIGHTCYAN_EX + self._shape[temp] + '\x1b[0m'
                elif(self.__spacevalue==1):
                    grid[i][j]=Fore.YELLOW + self._shape[temp] + '\x1b[0m'

    def generate_path_for_dragon(self,grid):
        tempx=14
        tempy=0
        self.__addx=[]
        self.__addy=[]
        for_four=0
        if(self._y>-1):
            while tempy < (self._y+self.__board_present_y):
                for_four+=1
                if(for_four==25):
                    for_four=5

                self.__addx.append(tempx)
                self.__addy.append(tempy)
                # grid[temp[0]][temp[1]]='c'
                if(for_four>=0 and for_four<5):
                    tempx+=1
                    tempy+=1
                elif(for_four>=5 and for_four<15):
                    tempx-=1
                    tempy+=1
                elif(for_four>=15 and for_four<25):
                    tempx+=1
                    tempy+=1

        if(tempx>self._x):
            while tempx>self._x:
                tempx-=1
                self.__addx.append(tempx)
                self.__addy.append(tempy)

        elif(tempx<=self._x):
            while tempx<self._x:
                tempx+=1
                self.__addx.append(tempx)
                self.__addy.append(tempy)

    def create_dragon_on_path(self,grid):  
        grid[self._x][self._y]="-"          
        grid[self._x][self._y+1]=" "          
        grid[self._x][self._y+2]=" "          
        grid[self._x+1][self._y]="*"          
        grid[self._x+1][self._y+1]="\\"          
        grid[self._x+1][self._y+2]=" "          
        grid[self._x+2][self._y]="`"          
        grid[self._x+2][self._y+1]="-"          
        grid[self._x+2][self._y+2]="'"          
        for i in range(len(self.__addx)-2):
            grid[self.__addx[i]][self.__addy[i]-self.__board_present_y]=Fore.RED+ "0" + '\x1b[0m'
            grid[self.__addx[i]+1][self.__addy[i]-self.__board_present_y+1]=Fore.YELLOW+ "#" + '\x1b[0m'
            grid[self.__addx[i]-1][self.__addy[i]-self.__board_present_y-1]=Fore.LIGHTCYAN_EX+ "#" + '\x1b[0m'

    def remove_dragon_on_path(self,grid):
        grid[self._x][self._y]=" "          
        grid[self._x][self._y+1]="@"          
        grid[self._x][self._y+2]=" "          
        grid[self._x+1][self._y]="<"          
        grid[self._x+1][self._y+1]=":"          
        grid[self._x+1][self._y+2]=">"          
        grid[self._x+2][self._y]="/"          
        grid[self._x+2][self._y+1]=" "          
        grid[self._x+2][self._y+2]="\\"  
        for i in range(len(self.__addx)):
            grid[self.__addx[i]][self.__addy[i]-self.__board_present_y]=' '
            grid[self.__addx[i]+1][self.__addy[i]-self.__board_present_y+1]=' '
            grid[self.__addx[i]-1][self.__addy[i]-self.__board_present_y-1]=' '

    # def create_wiggle_down(self,grid):     
    #     for i in range(len(self.__addx)):
    #         grid[self.__addx[i]][self.__addy[i]-self.__board_present_y]=' '
    #         grid[self.__addx[i]+1][self.__addy[i]-self.__board_present_y+1]=' '
    #         grid[self.__addx[i]-1][self.__addy[i]-self.__board_present_y-1]=' '       
    #     for i in range(len(self.__addx)):
    #         grid[self.__addx[i]+1][self.__addy[i]-self.__board_present_y]='0'
    #         grid[self.__addx[i]+2][self.__addy[i]-self.__board_present_y+1]='0'
    #         grid[self.__addx[i]][self.__addy[i]-self.__board_present_y-1]='0'

    # def remove_wiggle_down(self,grid):
    #     for i in range(len(self.__addx)):
    #         grid[self.__addx[i]+1][self.__addy[i]-self.__board_present_y]=' '
    #         grid[self.__addx[i]+2][self.__addy[i]-self.__board_present_y+1]=' '
    #         grid[self.__addx[i]][self.__addy[i]-self.__board_present_y-1]=' '
    #     self.create_dragon_on_path(grid)

    # def create_wiggle_up(self,grid):     
    #     for i in range(len(self.__addx)):
    #         grid[self.__addx[i]][self.__addy[i]-self.__board_present_y]=' '
    #         grid[self.__addx[i]+1][self.__addy[i]-self.__board_present_y+1]=' '
    #         grid[self.__addx[i]-1][self.__addy[i]-self.__board_present_y-1]=' '       
    #     for i in range(len(self.__addx)):
    #         grid[self.__addx[i]-1][self.__addy[i]-self.__board_present_y]='0'
    #         grid[self.__addx[i]][self.__addy[i]-self.__board_present_y+1]='0'
    #         grid[self.__addx[i]-2][self.__addy[i]-self.__board_present_y-1]='0'

    # def remove_wiggle_up(self,grid):
    #     for i in range(len(self.__addx)):
    #         grid[self.__addx[i]-1][self.__addy[i]-self.__board_present_y]=' '
    #         grid[self.__addx[i]][self.__addy[i]-self.__board_present_y+1]=' '
    #         grid[self.__addx[i]-2][self.__addy[i]-self.__board_present_y-1]=' '
    #     self.create_dragon_on_path(grid)