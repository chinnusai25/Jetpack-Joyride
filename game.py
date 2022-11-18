import signal,os,time,random

from alarmexception import AlarmException
from getch import _getChUnix as getChar
from board import Board
from mandalorian import Mandalorian
from scenary import Scenary
from extra_stuff import Extra_stuff
from enemy import Enemy
from colorama import init, Fore

#Creation of objects and accessing methods

#Setting up board(i.e grid)
board=Board(30,500)
board.createboard()

#Setting up HERO
mandalorian=Mandalorian(25,0)
mandalorian.shape()
mandalorian.start(board.matrix)

dragon_show_width=0

#Setting up Scenary
s=Scenary()
s.create_ground(board.matrix)
s.create_sky(board.matrix)
s.create_beams_horizontal(board.matrix,random.randint(1,7),random.randint(10,27))
s.create_beams_vertical(board.matrix,random.randint(8,16),random.randint(30,60))
s.create_beams_slant(board.matrix,random.randint(17,20),random.randint(65,80))

#Creation of coins using method create_coins
tempxx=0
tempyy=0
for i in range(7):
    tempxx=random.randint(4,24)
    tempyy+=random.randint(14,47)+20
    s.create_coins(board.matrix,tempxx,tempyy)

#Creation of speedups(S) using method create_speedup
tempxx=0
tempyy=0
for i in range(4):
    tempxx=random.randint(4,24)
    tempyy+=random.randint(14,42)+25
    s.create_speedup(board.matrix,tempxx,tempyy)

#Creation of enemies(on ground) using class Enemy and method start
tempxx=0
tempyy=0
for i in range(15):
    tempxx=26
    tempyy+=random.randint(10,25)+4
    enemy1=Enemy(tempxx,tempyy)
    enemy1.shape()
    enemy1.start(board.matrix)

#Printing the setup
board.print()

is_any_button_pressed=0

#Creation of magnets using method create_magnet
extra_stuff=Extra_stuff()

tempxx=0
tempyy=0
for i in range(1):
    tempxx=1
    tempyy+=random.randint(30,130)
    extra_stuff.create_magnet(board.matrix,tempxx,tempyy)

#Function for movement of mandalorian
def mand_move():
    def alarmhandler(signum,frame):
        raise AlarmException
    def user_input(timeout=0.1):
        signal.signal(signal.SIGALRM,alarmhandler)
        signal.setitimer(signal.ITIMER_REAL,timeout)

        try:
            text=getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM,signal.SIG_IGN)
        return ''

    char=user_input()
    
    if(char=='o'):
        mandalorian.generate_path_for_dragon(board.matrix)
        mandalorian.create_dragon_on_path(board.matrix)
        extra_stuff.set_o_pressed()

    if(char=='d'):
        is_any_button_pressed=1
        is_it_safe=mandalorian.safety_check_at_right_move(board.matrix) #Checking for collisions 
        here= extra_stuff.spacevalue()  #checking if shield activated
        if(is_it_safe==1 and here==0):
            mandalorian.need_to_be_updated(board.matrix)
            mandalorian.set_x(25)
            mandalorian.set_y((mandalorian.get_y()+4)%100)
            mandalorian.is_updated(board.matrix)
            mandalorian.decrease_lives()
            if(mandalorian.lives_left()==0):
                print("GAME OVER")
                quit()
        else:
            if(mandalorian.get_y()<107):    #checking for coins , speedups and YODHA and updating appropriately
                if( board.matrix[mandalorian.get_x()][mandalorian.get_y()+3]==Fore.YELLOW+ "$" + '\x1b[0m' 
                    or board.matrix[mandalorian.get_x()+1][mandalorian.get_y()+3]==Fore.YELLOW+ "$" + '\x1b[0m'  
                    or board.matrix[mandalorian.get_x()+2][mandalorian.get_y()+3]==Fore.YELLOW+ "$" + '\x1b[0m'):
                    mandalorian.increase_coins()

                if( board.matrix[mandalorian.get_x()][mandalorian.get_y()+3]=='S' 
                    or board.matrix[mandalorian.get_x()+1][mandalorian.get_y()+3]=='S'  
                    or board.matrix[mandalorian.get_x()+2][mandalorian.get_y()+3]=='S'):
                    extra_stuff.setspeedup()
                    extra_stuff.set_speedup_start_time( extra_stuff.remaining_time)

                if( board.matrix[mandalorian.get_x()][mandalorian.get_y()+3]==':' 
                    or board.matrix[mandalorian.get_x()+1][mandalorian.get_y()+3]==':'  
                    or board.matrix[mandalorian.get_x()+2][mandalorian.get_y()+3]==':' and won==1):
                    print("KUDOS!!!YOU WON")
                    quit()

                mandalorian.need_to_be_updated(board.matrix)
                mandalorian.set_y(mandalorian.get_y()+1)
                mandalorian.is_updated(board.matrix)
            else:
                pass  
        
        if(extra_stuff.get_o_pressed()==1):
            mandalorian.remove_dragon_on_path(board.matrix)
            mandalorian.generate_path_for_dragon(board.matrix)
            mandalorian.create_dragon_on_path(board.matrix)  

    if(char=='a'):
        is_any_button_pressed=1
        is_it_safe=mandalorian.safety_check_at_left_move(board.matrix)
        here=extra_stuff.spacevalue()
        if(is_it_safe==1 and (here==0)):
            mandalorian.need_to_be_updated(board.matrix)
            mandalorian.set_x(25)
            mandalorian.set_y((mandalorian.get_y()-4)%100)
            mandalorian.is_updated(board.matrix)
            mandalorian.decrease_lives()
            if(mandalorian.lives_left()==0):
                print("GAME OVER")
                quit()
        else:
            if(mandalorian.get_y()>0):
                if( board.matrix[mandalorian.get_x()][mandalorian.get_y()-1]==Fore.YELLOW+ "$" + '\x1b[0m'
                    or board.matrix[mandalorian.get_x()+1][mandalorian.get_y()-1]==Fore.YELLOW+ "$" + '\x1b[0m' 
                    or board.matrix[mandalorian.get_x()+2][mandalorian.get_y()-1]==Fore.YELLOW+ "$" + '\x1b[0m'):
                    mandalorian.increase_coins()

                if( board.matrix[mandalorian.get_x()][mandalorian.get_y()-1]=='S'
                    or board.matrix[mandalorian.get_x()+1][mandalorian.get_y()-1]=='S' 
                    or board.matrix[mandalorian.get_x()+2][mandalorian.get_y()-1]=='S'):
                    extra_stuff.setspeedup()  
                    extra_stuff.set_speedup_start_time( extra_stuff.remaining_time)

                if( board.matrix[mandalorian.get_x()][mandalorian.get_y()-1]==':'
                    or board.matrix[mandalorian.get_x()+1][mandalorian.get_y()-1]==':' 
                    or board.matrix[mandalorian.get_x()+2][mandalorian.get_y()-1]==':' and won==1):
                    print("KUDOS!!!YOU WON")
                    quit()
                
                mandalorian.need_to_be_updated(board.matrix)
                mandalorian.set_y(mandalorian.get_y()-1)                
                mandalorian.is_updated(board.matrix)
            else:
                pass    
        
        if(extra_stuff.get_o_pressed()==1):
            mandalorian.remove_dragon_on_path(board.matrix)
            mandalorian.generate_path_for_dragon(board.matrix)
            mandalorian.create_dragon_on_path(board.matrix)  
        
    if(char=='w'):
        is_any_button_pressed=1
        is_it_safe=mandalorian.safety_check_at_up_move(board.matrix)
        here=extra_stuff.spacevalue()
        if(is_it_safe==1 and here==0):
            mandalorian.need_to_be_updated(board.matrix)
            mandalorian.set_x(25)
            mandalorian.is_updated(board.matrix)
            mandalorian.decrease_lives()
            if(mandalorian.lives_left()==0):
                print("GAME OVER")
                quit()
        else:
            if(mandalorian.get_x()>1 and mandalorian.get_x()<=28):   
                if( board.matrix[mandalorian.get_x()-1][mandalorian.get_y()]==Fore.YELLOW+ "$" + '\x1b[0m'
                    or board.matrix[mandalorian.get_x()-1][mandalorian.get_y()+1]==Fore.YELLOW+ "$" + '\x1b[0m'
                    or board.matrix[mandalorian.get_x()-1][mandalorian.get_y()+2]==Fore.YELLOW+ "$" + '\x1b[0m'):
                    mandalorian.increase_coins()  

                if( board.matrix[mandalorian.get_x()-1][mandalorian.get_y()]=='S'
                    or board.matrix[mandalorian.get_x()-1][mandalorian.get_y()+1]=='S'
                    or board.matrix[mandalorian.get_x()-1][mandalorian.get_y()+2]=='S'):
                    extra_stuff.setspeedup()   
                    extra_stuff.set_speedup_start_time( extra_stuff.remaining_time)
                
                if( board.matrix[mandalorian.get_x()-1][mandalorian.get_y()]==':'
                    or board.matrix[mandalorian.get_x()-1][mandalorian.get_y()+1]==':'
                    or board.matrix[mandalorian.get_x()-1][mandalorian.get_y()+2]==':' and won==1):
                    print("KUDOS!!!YOU WON")
                    quit()

                if(board.matrix[mandalorian.get_x()-1][mandalorian.get_y()]!='M'):

                    mandalorian.need_to_be_updated(board.matrix)
                    mandalorian.set_x(mandalorian.get_x()-1)                
                    mandalorian.is_updated(board.matrix)
            else:
                pass
        
        if(extra_stuff.get_o_pressed()==1):
            mandalorian.remove_dragon_on_path(board.matrix)
            mandalorian.generate_path_for_dragon(board.matrix)
            mandalorian.create_dragon_on_path(board.matrix)  
        
    if (char==' ' and (extra_stuff.get_space_button_start_time()-extra_stuff.remaining_time>=15)): #Shield activation on space press
        extra_stuff.setspace()
        mandalorian.setspace()
        mandalorian.is_updated(board.matrix)
        extra_stuff.set_space_button_start_time( extra_stuff.remaining_time-10)
        
    if(char=='b'):      #Bullets release
        extra_stuff.set_no_of_bullets()
        extra_stuff.add_xcoo_of_bullets(mandalorian.get_x()+1)
        extra_stuff.create_bullet(board.matrix,mandalorian.get_x()+1,mandalorian.get_y()+3)

    if(char=='i'):
        mandalorian.remove_dragon_on_path(board.matrix)
        extra_stuff.unset_o_pressed()

    if(char=='q'):      #Quit
        is_any_button_pressed=1
        quit()

#Variables for playing with time
x=round(time.time())
y=x
z=x
time1=x
gametime=x
bullettime=x
dragontime=x
dragon_appear_time=x
iceball_start_time=x
iceball_move_time=x
magnet_time=x
won=0   #Variable to say dragon is defeated

while True:

    os.system('tput reset')

    extra_stuff.remaining_time=100-(round(time.time()-round(gametime))) #Updating remaining time of game
    if( extra_stuff.remaining_time<=0):
        print("TIME ENDS..\n\nGAME FINISHED")
        quit()

    here=extra_stuff.get_space_button_start_time()
    if(extra_stuff.get_dragon_lives_left()==0 and not won):     #If dragon is dead displaying YODHA
        won=1
        s.clear_dragon(board.matrix,s.drx,s.dry)
        s.create_yoda(board.matrix,s.drx,s.dry+8)

    if(mandalorian.lives_left()==0):        #If mando is dead game lost
        print("YOUR LIVES ARE NO MORE\nNEXT TIME MAY BE THE FORCE IS WITH YOU!!!!!")
        quit()

    if(((here- extra_stuff.remaining_time)==extra_stuff.get_shield_threshold_time() and (extra_stuff.spacevalue()==1))):
        extra_stuff.unsetspace()            #Deactivation of shield after 10 secs
        mandalorian.unsetspace()
        mandalorian.is_updated(board.matrix)

    if(extra_stuff.get_speedup_start_time()- extra_stuff.remaining_time==10):       #Deactivating speed up after 10 secs
        extra_stuff.unsetspeedup()
        extra_stuff.set_speedup_start_time(0)

    #Display on TOP
    print('Time left', extra_stuff.remaining_time,'\t\t\t\t','Lives left',mandalorian.lives_left())
    print('score',mandalorian.no_of_coins_collected()+extra_stuff.get_extra_score(),'\t\t\t',"dragon lives left",extra_stuff.get_dragon_lives_left())
    if(extra_stuff.get_space_button_start_time()-extra_stuff.remaining_time>=15):
        print("SHIELD IS ACTIVATED(PRESS SPACE TO ACTIVATE)")
    else:
        print()
    if( extra_stuff.remaining_time<=100-extra_stuff.dragon_start()+3 and won==0):
        print("BE READY TO FACE THE BOSS ENEMY!!!\t\t   STAY LEFT...")
    elif(won==1):
        print("GREAT FIGHT!!!\tBOSS ENEMY IS DEFEATED\tTOUCH YODHA TO FINISH THE GAME")
    else:
        print('\n')


    temp=[None]*50
    no_mandolarian_move=0
    if(extra_stuff.getspeedup()==1):
        moving_time_threshold=0.09
    else:
        moving_time_threshold=0.75 
    
    # checking if mandalorian is at corner
    tem=0
    if(time.time()-bullettime>=0.001): #movement of bullet

        bullets_xcoo_array=extra_stuff.get_xcoo_of_bullets()
        for i in range (len(bullets_xcoo_array)):
            extra_stuff.move_bullets(board.matrix,bullets_xcoo_array[i])
        bullettime=time.time()

    #movement of iceballs
    if(time.time()-iceball_move_time>=0.005):    
        iceballs_xcoo_array=extra_stuff.get_xcoo_of_iceballs()
        for i in range (len(iceballs_xcoo_array)):
            should_lives_decrease=extra_stuff.move_iceballs(board.matrix,iceballs_xcoo_array[i])
            if(should_lives_decrease==1):
                mandalorian.decrease_lives()
        iceball_move_time=time.time()                

    #bg movement
    if((time.time())-z>=moving_time_threshold):
        mandalorian.set_board_present_y()
        
        if(mandalorian.get_y()>0 and mandalorian.get_y()<=107):
            mandalorian.set_y(mandalorian.get_y()-1)
        else:
            no_mandolarian_move=1    
        for k in range(0,29,1):
            if(no_mandolarian_move==1):
                pass
            else:
                temp[k]=board.matrix[k][0]

        for i in range(0,498,1):        #not moving mandalorian if at corner and moving the scenary
            for j in range(0,29,1):
                if(no_mandolarian_move and (mandalorian.get_y()==i or mandalorian.get_y()+1==i or mandalorian.get_y()+2==i) and (mandalorian.get_x()==j or mandalorian.get_x()+1==j or mandalorian.get_x()+2==j)):
                    pass
                else:
                    if(board.matrix[j][i+1]=='=' or board.matrix[j][i]=='='):
                        pass
                    else:
                        board.matrix[j][i]=board.matrix[j][i+1]

        extra_stuff.set_magnet_pos()
        
        for k in range(0,29,1):             #Appending first row last
            board.matrix[k][499]=temp[k] 

        z=(time.time())   
    
        is_it_safe=mandalorian.safety_check_at_right_move(board.matrix) #Checking of obstacles as hero is not moving at corner
        here= extra_stuff.spacevalue()
        if(is_it_safe==1 and here==0):
            mandalorian.need_to_be_updated(board.matrix)
            mandalorian.set_x(25)
            mandalorian.set_y(mandalorian.get_y()+8)
            mandalorian.is_updated(board.matrix)
            mandalorian.decrease_lives()
            if(mandalorian.lives_left()==0):
                print("GAME OVER")
                quit()    

    #Display of dragon after extra_stuff.dragon_start()
    if(time.time()-dragon_appear_time>=extra_stuff.dragon_start() and time.time()-time1>=0.3 and extra_stuff.get_dragon_lives_left()>0):
        
        if(s.dry!=0):
            s.clear_dragon(board.matrix,s.drx,s.dry)    #Dragon needs to be cleared and made appeared again as it shouldnt move left 

        if(mandalorian.get_x()<=12):
            s.drx=2
            s.dry=107-(dragon_show_width)
            s.create_dragon(board.matrix,s.drx,s.dry)
        else:
            s.drx=mandalorian.get_x()-11
            s.dry=107-(dragon_show_width)
            s.create_dragon(board.matrix,s.drx,s.dry)

        if(round(time.time())-iceball_start_time>=2):
            extra_stuff.set_no_of_iceballs()
            extra_stuff.add_xcoo_of_iceballs(mandalorian.get_x()+1)
            extra_stuff.create_iceballs(board.matrix,mandalorian.get_x()+1,65)
            iceball_start_time=round(time.time())

        if(mandalorian.get_y()>=108-dragon_show_width and extra_stuff.spacevalue()==0): #FIRE as hero touched dragon
            print("FIRE AS YOU TOUCHED DRAGON!!!!")
            quit()

        if(dragon_show_width<=s.dragon_width):
            dragon_show_width+=1                    #Dragon appearing/moving towards left slowly
        time1=time.time()

    #magnet checking
    if(time.time()-dragontime>=0.03):   
        if(extra_stuff.get_magnet_pos()-mandalorian.get_y()>0 and extra_stuff.get_magnet_pos()-mandalorian.get_y()<=15):
            is_it_safe=mandalorian.safety_check_at_right_move(board.matrix)
            here= extra_stuff.spacevalue()
            if(is_it_safe==1 and here==0):
                mandalorian.need_to_be_updated(board.matrix)
                mandalorian.set_x(25)
                mandalorian.set_y(mandalorian.get_y()+1)
                mandalorian.is_updated(board.matrix)
                mandalorian.decrease_lives()
                if(mandalorian.lives_left()==0):
                    print("GAME OVER")
                    quit()
            else:
                if(mandalorian.get_y()<107):
                    if( board.matrix[mandalorian.get_x()][mandalorian.get_y()+3]==Fore.YELLOW+ "$" + '\x1b[0m' 
                        or board.matrix[mandalorian.get_x()+1][mandalorian.get_y()+3]==Fore.YELLOW+ "$" + '\x1b[0m'  
                        or board.matrix[mandalorian.get_x()+2][mandalorian.get_y()+3]==Fore.YELLOW+ "$" + '\x1b[0m'):
                        mandalorian.increase_coins()

                    if( board.matrix[mandalorian.get_x()][mandalorian.get_y()+3]=='S' 
                        or board.matrix[mandalorian.get_x()+1][mandalorian.get_y()+3]=='S'  
                        or board.matrix[mandalorian.get_x()+2][mandalorian.get_y()+3]=='S'):
                        extra_stuff.setspeedup()
                        extra_stuff.set_speedup_start_time( extra_stuff.remaining_time)

                    mandalorian.need_to_be_updated(board.matrix)
                    mandalorian.set_y(mandalorian.get_y()+1)
                    mandalorian.is_updated(board.matrix)
                else:
                    pass

        if(extra_stuff.get_magnet_pos()-mandalorian.get_y()<0 and extra_stuff.get_magnet_pos()-mandalorian.get_y()>=-15):
            is_it_safe=mandalorian.safety_check_at_left_move(board.matrix)
            here=extra_stuff.spacevalue()
            if(is_it_safe==1 and (here==0)):
                mandalorian.need_to_be_updated(board.matrix)
                mandalorian.set_x(25)
                mandalorian.set_y(mandalorian.get_y()-1)
                mandalorian.is_updated(board.matrix)
                mandalorian.decrease_lives()
                if(mandalorian.lives_left()==0):
                    print("GAME OVER")
                    quit()
            else:
                if(mandalorian.get_y()>0):
                    if( board.matrix[mandalorian.get_x()][mandalorian.get_y()-1]==Fore.YELLOW+ "$" + '\x1b[0m'
                        or board.matrix[mandalorian.get_x()+1][mandalorian.get_y()-1]==Fore.YELLOW+ "$" + '\x1b[0m' 
                        or board.matrix[mandalorian.get_x()+2][mandalorian.get_y()-1]==Fore.YELLOW+ "$" + '\x1b[0m'):
                        mandalorian.increase_coins()

                    if( board.matrix[mandalorian.get_x()][mandalorian.get_y()-1]=='S'
                        or board.matrix[mandalorian.get_x()+1][mandalorian.get_y()-1]=='S' 
                        or board.matrix[mandalorian.get_x()+2][mandalorian.get_y()-1]=='S'):
                        extra_stuff.setspeedup()  
                        extra_stuff.set_speedup_start_time( extra_stuff.remaining_time)

                    mandalorian.need_to_be_updated(board.matrix)
                    mandalorian.set_y(mandalorian.get_y()-1)
                    mandalorian.is_updated(board.matrix)
                else:
                    pass    
        dragontime=time.time()
    
    #Printing the above movements
    board.print()
    is_any_button_pressed=0
    #Calling function described above
    mand_move()
    
    #mario moving down
    is_it_safe=mandalorian.safety_check_at_down_move(board.matrix)
    if(is_it_safe==1 and (not extra_stuff.spacevalue())):
        mandalorian.need_to_be_updated(board.matrix)
        mandalorian.set_x(25)
        mandalorian.is_updated(board.matrix)
        mandalorian.decrease_lives()
        if(mandalorian.lives_left()==0):
            print("GAME OVER")
            quit()
        
    #Gravity Effect
    if(time.time()-y>=(30-mandalorian.get_x())/140):
        is_it_safe=mandalorian.safety_check_at_down_move(board.matrix)
        if(is_it_safe==1 and (extra_stuff.spacevalue()==0)):
            mandalorian.need_to_be_updated(board.matrix)
            mandalorian.set_x(25)
            mandalorian.is_updated(board.matrix)
            mandalorian.decrease_lives()
            if(mandalorian.lives_left()==0):
                print("GAME OVER")
                quit()
        else:
            if(mandalorian.get_x()>=1 and mandalorian.get_x()<25):   
                if( board.matrix[mandalorian.get_x()+3][mandalorian.get_y()]==Fore.YELLOW+ "$" + '\x1b[0m'
                    or board.matrix[mandalorian.get_x()+3][mandalorian.get_y()+1]==Fore.YELLOW+ "$" + '\x1b[0m'
                    or board.matrix[mandalorian.get_x()+3][mandalorian.get_y()+2]==Fore.YELLOW+ "$" + '\x1b[0m'):
                    mandalorian.increase_coins()  

                if( board.matrix[mandalorian.get_x()+3][mandalorian.get_y()]=='S'
                    or board.matrix[mandalorian.get_x()+3][mandalorian.get_y()+1]=='S'
                    or board.matrix[mandalorian.get_x()+3][mandalorian.get_y()+2]=='S'):
                    extra_stuff.setspeedup()   
                    extra_stuff.set_speedup_start_time( extra_stuff.remaining_time)
                
                if( board.matrix[mandalorian.get_x()+3][mandalorian.get_y()]==':'
                    or board.matrix[mandalorian.get_x()+3][mandalorian.get_y()+1]==':'
                    or board.matrix[mandalorian.get_x()+3][mandalorian.get_y()+2]==':' and won==1):
                    print("KUDOS!!!YOU WON")
                    quit()

                mandalorian.need_to_be_updated(board.matrix)
                mandalorian.set_x(mandalorian.get_x()+1)                
                mandalorian.is_updated(board.matrix)    
        
        if(extra_stuff.get_o_pressed()==1):
            mandalorian.remove_dragon_on_path(board.matrix)
            mandalorian.generate_path_for_dragon(board.matrix)
            mandalorian.create_dragon_on_path(board.matrix)  

        y=time.time()


