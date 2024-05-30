import random
import turtle
from turtle import *

screen=Screen()
screen.setup(800,800)
screen.bgcolor("lightblue")

t=Turtle()
t.width(5)


##CONSTANTS##
RIGHT_EDGE=350
LEFT_EDGE=-350
BOTTOM_EDGE=-350
TOP_EDGE=350

DO_NOTHING=-1
PRINT_STATEMENT=0
ASK_FOR_INPUT=1

PATH=0
WALL=1
PLANK=2
DOOR=3
RIVER=4
APPLE=5
POWERUP=6
OGRE=7
WINGAME=8
PLAYER=9
DECODE=10

##VARIABLES##
powerUpTurn=5  #how many turns they have if they find the power up
gamePlay=False #start the game loop as false because we ask if they want to play
power=False    #start the power up as false because they do not start with the power up

#for encription and decription 
s1="YOU FIGURED IT OUT"  #they must decode this phrase which will be mixed up
s2= ""


#list of players inventory
inventory=[
            ["apples",0],
            ["planks",0]
            ]



Map = [
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 2, 4, 4, 4, 4, 1, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 0, 1, 10, 1, 4, 4, 1, 0, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 6, 1, 3, 0, 4, 4, 1, 0, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 1, 0, 1, 0, 4, 4, 0, 0, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 1, 0, 1, 0, 4, 4, 0, 0, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 0, 0, 1, 0, 4, 4, 0, 0, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 0, 0, 1, 0, 4, 4, 0, 0, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 0, 0, 1, 0, 4, 4, 0, 0, 0, 0, 0, 7, 8, 1],
            [ 1, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 7, 8, 1],
            [ 1, 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 7, 8, 1],
            [ 1, 0, 0, 1, 4, 4, 4, 4, 4, 4, 0, 0, 0, 7, 8, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            
	]

#list of all the possible events that can happen on each spot
eventList= [[DO_NOTHING, 0, "peru", "You are on the path","   "],
	    [DO_NOTHING, 1, "brown", "Wall","1  "],
	    [ASK_FOR_INPUT, 2, "peru", "You found a plank, do you want to pick it up? y/n","   "],
	    [PRINT_STATEMENT, 3,"burlywood","You've come to a door.","   "],
	    [PRINT_STATEMENT, 4,"blue", "Theres a river in your way",")( "],
	    [PRINT_STATEMENT, 5,"red", "You found fruit.","@  "],
            [PRINT_STATEMENT, 6, "peru","You found a power up that shows you where all the planks are hiding, but it only lasts for 5 moves,","   "], #if they land on this square, which has a 50% chance of spawning, they are able to see all the planks for 3 moves 
            [ASK_FOR_INPUT, 7, "darkgreen", "There is an ogre blocking your path, you must feed him 5 apples to pass,", "): " ,"Do you want to give the ogre your apples to pass? y/n"],
            [PRINT_STATEMENT, 8, "peru","YOU WIN!!!","   "], #if they make it to the spots that are equal to 8, you win            
            [DO_NOTHING, 9, "white", "This is where you are.", "* "],
            [PRINT_STATEMENT, 10, "yellow", "You mush decode:",s2,"It is incripted by a shifter of 3.","   "]
            ]


sideheight=700/len(Map)  #so that no matter how many rows of the map, its always gonna be in the middle
sidelen=700/len(Map[0])  #same as the one above but size is based on how many columns are in the top row is


##FUNCTIONS##

def encriptString(string):
    global s2
    for char in range(len(s1)):
        s2Char=ord(string[char])
        s2Char=s2Char-3
        s2=s2+(chr(s2Char))
        if Map[currX][currY]==DECODE:
            print(chr(s2Char), end="")
    print()
    return(s2)

def draw_box(row,col,x,y): #draws individual squares for graphical map
    t.seth(0)
    t.fillcolor(eventList[Map[row][col]][2])
    if (x == col) and (y == row):   #white square if this is where player is
       t.fillcolor("white")
    t.begin_fill()
    for square in range(0,2):
        t.forward(sidelen)
        t.rt(90)
        t.forward(sideheight)
        t.rt(90)
    t.forward(sidelen)
    t.end_fill()

def draw_turtle_map():  #draw graphical turtle map
    #t.penup()
    start_x=(LEFT_EDGE)
    start_y=(TOP_EDGE)
    t.pendown()
    for row in range(0,len(Map)):
        t.goto(start_x,start_y)
        for col in range(0,len(Map[row])):
            t.pendown()
            draw_box(row,col,currX, currY)
            start_x=start_x+sidelen
        start_x=LEFT_EDGE
        start_y=start_y-sidelen
        t.penup()
        t.hideturtle()


#define a function to print the starting statements at the beginning of the game
def starting_statements():
    print("Welcome to Apples and Ogres!")
    print()
    print("You are trapped in a forest, to escape you must build a bridge to cross the river and feed the ogre.")
    print("Find planks hidden around the map to build a bridge to cross the river safely")
    print("If you are lucky, you may find a power up that shows you where the planks are hidden.")
    print("Collect 5 apples (@) to satisfy the ogre ): so he will let you pass.")
    print("You are the white square or *")
    print()
    gameStart=input("Are you ready to play? y/n")
    return(gameStart)


#Define a function to print our Map and current Player location
def drawMap(currX, currY):  #text game map
    #print ("map size is : ", len(Map), " rows by ", len(Map[0]), " columns")
    print()
    for y in range (0, len(Map)):
        for x in range (0,len(Map[y])):
            if (currX == x) and (currY == y):   #print * if they are in this square
                print("*  ", end="")
                #Map[currY][currX]=9
                continue
            
            if Map[y][x]==2 and power==True: #print - for the plank if they have the powerup
                print("-  ", end="")
                continue
            
            print (eventList[Map[y][x]][4], end ="") #print everything else
        print()
    print()

       
def movePlayer(x,y,moveDir):
    #assume invalid move is attempted
    badMove = True

    #Now check if the move is valid - brute force method - better ways exist
    if moveDir == "u" and Map[y-1][x] != 1:
            #print ("valid up move")
            power_up(x,y)
            return (x, y-1)

    if moveDir == "d"and Map[y+1][x] != 1:
            power_up(x,y)
            #print ("valid down move")
            return (x, y+1)

    if moveDir == "l"and Map[y][x-1] != 1:
            power_up(x,y)
            #print ("valid left move")
            return (x-1, y)

    if moveDir == "r"and Map[y][x+1] != 1:
            power_up(x,y)
            #print ("valid right move")
            return (x+1, y)
         
    #they attempted a bad move
    if badMove:
        print ("**Invalid move** Try again.")
        return (x,y)   #return the same location they are in since no move


#check to see if the space the player is on is a special event besides wall or path
def check_Event (x, y):
    global currX, gamePlay
    if Map[y][x]!=-1 and Map[y][x]!=0:
        
        if Map[y][x]==RIVER:
            print ("You cant go through the river unless you find a plank")
            
            if inventory[1][1]>=1:
                usePlank=input("you have a plank, would you like to use it to cross the river? y/n")

                if usePlank=="y":
                    inventory[1][1]=inventory[1][1]-1
                    Map[y][x]= 0
                    return
        
            currX=currX-1
            return (currX)
            
        if eventList[Map[y][x]][0]==ASK_FOR_INPUT: #if first object in list is ASK_FOR_INPUT
            if Map[y][x]==OGRE: #check first if it is an ogre
                if inventory[0][1]>=5: # then check if they have enough apples to feed it
                    giveApple=input(eventList[Map[y][x]][5]) #ask if they want to feed the ogre their apples
                    if giveApple=="y":
                        inventory[0][1]=inventory[0][1]-5
                        Map[y][x]=0
                        return
                    
                    currX=currX-1                 
                    return
                
                else: #if they dont have enough apples then they cannot pass
                    print(eventList[Map[y][x]][3])
                    currX=currX-1
                    return

##            t.goto(0,0)
##            t.color("white")
##            t.write(("You found a",inventory[Map[y][x]-1][1]),"!!!", font=("Times New Roman", 25,"normal"))
##            t.color("black")
                
            answer=input(eventList[Map[y][x]][3])
            
            if answer== "y":
                inventory[Map[y][x]-1][1]=inventory[Map[y][x]-1][1]+1 
                Map[y][x]=0
                
            return
            
        if eventList[Map[y][x]][0]==PRINT_STATEMENT: #if first object in list is PRINT_STATEMENT
            print(eventList[Map[y][x]][3])
            if Map[x][y]==DECODE:
                player_decode()
            if Map[y][x]==WINGAME: #if they make it to an 8 they win
                gamePlay=False
                return(gamePlay)                 
    return

def player_decode():
    print("You must decode,", s2)
    print("it is encoded with a shifter function of 3")
    guess=input("what is your guess?")
    if guess==s2:
        print("yay! you may pass")

			
#a function that adds fruit into random places around the left half of  map		
def add_fruit():
    #to place the appples randomly
    random_y_apple= random.randint(2,len(Map)-2)
    random_x_apple= random.randint(1,5)
    Map[random_y_apple][random_x_apple]=5


#a function that adds planks into random places around the left half of map    
def add_planks():
    # to place the planks randomly
    random_y_plank= random.randint(2,len(Map)-3)
    random_x_plank= random.randint(1,5)
    Map[random_y_plank][random_x_plank]=2
    
    
#to check if the player collected apples
def check_collisions(x,y):
    global inventory
    if Map[y][x]==APPLE:
        Map[y][x]=0
        inventory[0][1]=inventory[0][1]+1
        add_fruit()
        

#print the players inventory before each turn
def print_inventory():
    t.clear()
    t.penup()
    t.goto(LEFT_EDGE,TOP_EDGE)
    for x in range(0,len(inventory)):
        print("you have", inventory[x][1],inventory[x][0])
        t.pendown()
        t.write((inventory[x][0],":",inventory[x][1]), font=("Comic Sans", 25,"normal"))
        t.penup()
        t.goto(0,TOP_EDGE)
        t.penup()
        

#place power up in specific spot with 50% chance of spawning
def place_power_up():
    powerUp=random.randint(0,10)
    if powerUp<5:
        Map[4][2]=0
    return

#functions that checks first if you have the power up, then executes its purpose for 5 moves
def power_up(x,y):
    global powerUpTurn,power

    if Map[y][x]==POWERUP:
        print(eventList[Map[y][x]][2])
        Map[y][x]=0
        eventList[PLANK][2]="black"
        power=True
        
    if power==True:
        print("you have",powerUpTurn,"moves left for your power up.")
        powerUpTurn=powerUpTurn-1
        if powerUpTurn<0:
            power=False
            eventList[PLANK][2]="peru"
            
        return
    return


##MAIN PROGRAM##
        
#Set our starting location
currX = 1
currY = 4

#start the game if they want to play
game=starting_statements()
if game=="y":
    gamePlay=True

#change three of the spots on the map to a fruit and one to a power up if chance is greater that 50%
place_power_up()
for fruit in range(0,4):
    add_fruit()
    
for planks in range(0,4):
    add_planks()

    
#draw the map the first time before asking for a move
drawMap(currX, currY)
screen.tracer(0)
encriptString(s1)


#Let the player move around the map on the path until they reach the end of the game
while gamePlay==True:
    draw_turtle_map()
    screen.update()
    check_Event(currX,currY)
    check_collisions(currX,currY)
    print_inventory()
    moveDir = input("Enter direction (u,d,l,r): ")
    currX, currY = movePlayer(currX, currY, moveDir)
    drawMap(currX, currY)
    print(s2)
