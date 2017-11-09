If pip is not installed then run the following command

For python
sudo apt-get install python-pip
pip install -r requirements.txt

For python3
sudo apt-get install python3-pip
pip3 install -r requirements.txt

You need to install this to run the script
sudo apt-get install cpufrequtils

To run the script use
sudo ./run.sh 
(Make sure that run.sh is an executable file)

You can also run the code by:
python3 gameplay.py
python gameplay.py

Basic Controls:-
Move Left  : a
Move Right : d
Move Up    : w
Move down  : s
Drop Bomb  : b
Quit Game  : q

Game consists of 3 levels and there are 2 types of enemies, both of them have different speeds. A bomb can be dropped anywhere by the bomberman at the position where it is currently placed and it explodes after 3 secs of being dropped.
The explosion of the bomb (denoted by ‘e’) will spread to a total of 4 positions (not including the bomb position and not 
occupied by any wall) ​evenly around the bomb​. 'X' represents the wall, '/' represents the bricks, 'B' represents Bomberman ,
'E' represents Enemy of type1 and 'F' represents Enemy of type2.
  
This game 'Bomberman' is implemented in Python using OOP concepts.
Modularity:
Code has been divided into separate files rather than writing code in a
single file.
Board.py	: It contains Board class and basic functions like print_board,initialize_board and check_position.
Wall.py		: It contains Wall class and basic framework of the game.
Bomb.py		: It contains Bomb class and deals with explosions
Level.py	: It contains the details of different levels
Brick.py	: It contains Brick class, which are randomly added.
Person.py	: It contains Person class and common functions of Enemy and Bomberman 
Enemy.py	: It contains Enemy class and functions like add_enemy, enemy_movement etc.
Bomberman.py	: It contains Player class and its controls its movements
Getchunix.py	: It contains the code for getting char from keyboard without interupt
Timeout.py	: It contains Timeout Handler and Timeout class which are used to call a function after a specific period of time.
Gameplay.py	: It is the main file which clubes all the other and integrates all the different functions and classes.

Inheritance:
Board, Bomb, Level and Wall are separate classes and inherit object class provided by python.
Timeout class inherits from the Exception class provided by python.
Person and Brick classes inherits from Board class as they use check_position function.
Enemy and Bomberman classes inherits from Person class
Enemy1 and Enemy2 are two classes which inheriant from Enemy class
Gameplay doesn't have any classes as such.

Polymorphism:
There are two objects Enemy1 and Enemy2 both of which inheriant from Enemy class. Both of them contains the same function names as 
the Enemy class contained but the defination of function is different for both of them. Therefore, we can access them using the same 
method. So we can call their action using the same method.

Encapsulation:
In this code, I have tried to restrict access to methods and variables so as to prevent data from being modified by accident.
For example player lives has been encapsulated, methods that were not needed to be made public were made private and protected depending 
of scenerio. E.g. moveright,moveleft,moveup and movedown of enemy class have been protected so that they can only be accessed by its 
sub-classes, that is Enemy1 and Enemy2, but enemymotion has been made private so that only Enemy class can access it.



 



