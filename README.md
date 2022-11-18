JETPACK JOYRIDE
ASSIGNMENT 1 : THE MANDALORIAN (DASS)

By: Kalakonda Sai Shashank
    2018111016
    CSD

About Game:
The game resembles JETPACK JOYRIDE

Rules:
1)'a','w','d' keys for left,up,and right movement of mandalorian respectively.
2)As long as 'w' is pressed the mandalorian moves upwards,but as soon as it is released,mandalorian moves down as gravity comes into play.
3)You can increase your score by collecting coins in the path,killing enemies which stay on the ground or by shooting the obstacles(beams) with bullets(pressing 'b' for bullets(=)).
4)You get 5 lives and a time of 100 seconds
5)Magnet(M) appears in between which tries to attract you towards itself horizontally
6)In the end ,the boss enemy appears ,firing ice balls(<) ,which on striking mandalorian loses his life.
7)Mandalorian needs to defeat boss enemy by hitting bullets,until boss enemy loses all his lifes
8)Once he loses all his lifes YODHA appears,which on touching game finishes and you will be the WINNER!!!
9)If time ends or you lost all your lives the try next time and hope the force will be with you!!

Requirements
1)Python3
2)Colorama library

Instructions to play
1)python3 game.py
2)Controls
    a) w,a,d to move up,left,right respectively
    b) b for bullets
    c) space for shield which will be activated for 10 seconds and requires 15 seconds for using again
    d)Need to collect 'S' to get speed up activated(for 10 seconds and multiple speed ups are not ativated at a time)
    e)Magnet 'M' attracts you towards it horizontally,play safe

About Codes:
1)board.py consists of basic matrix code over which elements are placed.
2)enemy.py consists Enemy class which creates ground enemies
3)extra_stuff.py code consists Extra_stuff class which consists all special features
4)game.py contains the while loop where the game run continuosly
5)mandalorian.py consists Mandalorian class which is the reason for generating our Hero
6)person.py consists the class Person which is inherited by Enemy and Mandalorian classes
7)scenary.py consists the class Scenary which consits beams and coins creating methods

BONUS:
Press 'o' for experiencing ultimate dragon feature
Press 'i' for disabling the ultimate dragon feature

If  multiple bullets hit from same location then the speed of first bullet increases