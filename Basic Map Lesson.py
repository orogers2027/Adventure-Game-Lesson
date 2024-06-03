import random
import turtle
from turtle import *

screen=Screen()
screen.setup(800,800)
screen.bgcolor("lightblue")

#turtle
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
PAUSE_TIL_RIGHT=2

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
decode=True    #start with the decoder on so that they can guess

#I put the funtion here because it said encriptString was not defined unless it was here
def encriptString(string):
    s2=""
    for char in range(len(s1)):
        s2Char=ord(string[char])
        s2Char=s2Char+3
        s2=s2+(chr(s2Char))
    return(s2)


#for encription and decription 
s1="you figured it out"  #they must decode this phrase which will be mixed up
s2=encriptString(s1)    #This is going to be the mixed up phrase which they will have to decode


#list of players inventory
inventory=[
            ["apples",0],
            ["planks",0]
            ]


#our game map
Map = [
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 2, 4, 4, 4, 4, 1, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 0, 1, 10, 1, 4, 4, 1, 0, 0, 0, 0, 7, 8, 1],
	    [ 1, 0, 6, 1, 3, 1, 4, 4, 1, 0, 0, 0, 0, 7, 8, 1],
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
eventList= [[DO_NOTHING, 0, "peru", "You are on the path","   "], #path
	    [DO_NOTHING, 1, "brown", "Wall","1  "],  #walls
	    [ASK_FOR_INPUT, 2, "peru", "You found a plank, do you want to pick it up? y/n","   "], #plank
	    [PRINT_STATEMENT, 3,"burlywood","You've come to a door.","   "], #door, nothing happens, its just a door
	    [PRINT_STATEMENT, 4,"blue", "Theres a river in your way",")( "], #river
	    [PRINT_STATEMENT, 5,"red", "You found fruit.","@  "],
            [PRINT_STATEMENT, 6, "peru","You found a power up that shows you where all the planks are hiding, but it only lasts for 5 moves,","   "], #if they land on this square, which has a 50% chance of spawning, they are able to see all the planks for 3 moves 
            [ASK_FOR_INPUT, 7, "darkgreen", "There is an ogre blocking your path, you must feed him 5 apples to pass,", "): " ,"Do you want to give the ogre your apples to pass? y/n"],
            [PRINT_STATEMENT, 8, "peru","YOU WIN!!!","   "], #if they make it to the spots that are equal to 8, you win            
            [DO_NOTHING, 9, "white", "This is where you are.", "* "],  #where the player is
            [PAUSE_TIL_RIGHT, 10, "peru", ("You mush decode: "+ s2+  " Each letter is incripted by a shifter of 3.") ,"   "] #spot where player has to decode
            ]


sideheight=700/len(Map)  #so that no matter how many rows of the map, its always gonna be in the middle
sidelen=700/len(Map[0])  #same as the one above but size is based on how many columns are in the top row is


##FUNCTIONS##
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

#draws map in turtle graphic screen
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


#define a function to print the starting statements/instructions at the beginning of the game
def starting_statements():
    print("Welcome to Apples and Ogres!")
    print()
    print("You are trapped in a forest, to escape you must build a bridge to cross the river and feed the ogre.")
    print("Find planks hidden around the map to build a bridge to cross the river safely")
    print("If you are lucky, you may find a power up that shows you where the planks are hidden.")
    print("Collect 5 apples (@) to satisfy the ogre ): so he will let you pass.")
    print("You are the white square, the red squares are apples, blue is the river, and green is the ogres.")
    print("use the arrow keys to move")
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

#did not need this function for current version of game because I used onkey instead
###If the player cannot move due to a wall, the location will not be updated    
##def movePlayer(x,y,moveDir):
##
##    #assume invalid move is attempted
##    badMove = True
##
##    #Now check if the move is valid - brute force method - better ways exist
##    if moveDir == "u" and Map[y-1][x] != 1:
##            #print ("valid up move")
##            power_up(x,y)
##            return (x, y-1)
##
##    if moveDir == "d"and Map[y+1][x] != 1:
##            power_up(x,y)
##            #print ("valid down move")
##            return (x, y+1)
##
##    if moveDir == "l"and Map[y][x-1] != 1:
##            power_up(x,y)
##            #print ("valid left move")
##            return (x-1, y)
##
##    if moveDir == "r"and Map[y][x+1] != 1:
##            power_up(x,y)
##            #print ("valid right move")
##            return (x+1, y)
##         
##    #they attempted a bad move
##    if badMove:
##        print ("**Invalid move** Try again.")
##        return (x,y)   #return the same location they are in since no move


#check to see if the space the player is on is a special event besides wall or path
def check_Event (x, y):
    global currX, gamePlay, decode
    
    if Map[y][x]!=-1 and Map[y][x]!=0:
        
        if Map[y][x]==RIVER: #check if they are in the river
            
            
            if inventory[1][1]>=1: #if they have planks ask if they want to use them
                usePlank=turtle.textinput("Planks","you have a plank, would you like to use it to cross the river? y/n") #screen will pop up to ask

                if usePlank=="y": #if yes the river will become crosssable
                    inventory[1][1]=inventory[1][1]-1
                    Map[y][x]= 0
                    return
            turtle.textinput("Plank","You cant go through the river unless you find a plank") #screen will pop up to tell them
        
            currX=currX-1 #if they say no, they will move back a square, so no cheating occurs
            return (currX)
            
        if eventList[Map[y][x]][0]==ASK_FOR_INPUT: #if first object in list is ASK_FOR_INPUT
            if Map[y][x]==OGRE: #check first if it is an ogre
                
                if inventory[0][1]>=5: # then check if they have enough apples to feed it
                    Apple=eventList[Map[y][x]][5] #ask if they want to feed the ogre their apples
                    giveApple=turtle.textinput("Apples",Apple) #screen will pop up to ask
                    
                    if giveApple=="y": #if they do give apple they will be able to pass and 5 apples get subrated from their inventory
                        inventory[0][1]=inventory[0][1]-5
                        Map[y][x]=0
                        return
                    
                    currX=currX-1    #same thing so no cheating occurs (it moves them back so they don't cheat)             
                    return
                
                else: #if they dont have enough apples then they cannot pass
                    ogre=eventList[Map[y][x]][3]
                    turtle.textinput("Ogre",ogre)
                    currX=currX-1
                    return

            whatPrint=eventList[Map[y][x]][3] 
                
            answer=turtle.textinput("Pick Up",whatPrint) #its gonna ask if they want to pick up an item or not
            
            if answer== "y": #if they answer yes, it will add the item into their inventory and set the current square = to 0
                inventory[Map[y][x]-1][1]=inventory[Map[y][x]-1][1]+1 
                Map[y][x]=0
                return
            else:
                Map[y][x]=0
                add_planks()#if they say no it will get rid of that plank and randomly place it somewhere else
                #(to fix an issue I had earlier where it would keep asking til you said yes to picking up the plank)
                
            return
            
        if eventList[Map[y][x]][0]==PRINT_STATEMENT: #if first object in list is PRINT_STATEMENT
            #whatPrint=eventList[Map[y][x]][3]
            print(eventList[Map[y][x]][3])
            #turtle.textinput("Print",whatPrint)
            #I decided not to have it print when you collected fruit because it got annoying the little screen popping up
            #also if I had left this in, when you go on the door a screen, that you can't get rid of, pops up saying that you've come to a door.
            #the reason this happens is cause when you go over the fruit that spot becomes 0, but when you go over the door it stays a door,
            #so it just keeps printing that you came to a door.

            
            if Map[x][y]==DECODE:
                player_decode()
            if Map[y][x]==WINGAME: #if they make it to an 8 they win
                gamePlay=False
                return(gamePlay)

        if eventList[Map[y][x]][0]==PAUSE_TIL_RIGHT:
            wordss=eventList[Map[y][x]][3]
            
            while decode==True:
                guess=turtle.textinput(wordss,"# stand for spaces and | stands for y. It is encoded with a shifter function of 3. what is your guess:")
                if guess==s1:
                    print("That's right")
                    Map[y][x]=0
                    decode=False
                else:
                    print("Wrong, try again")
                print()   
    return


def player_decode():
    print("You must decode,", s2)
    print("")
    guess=turtle.textinput("Decode Time","it is encoded with a shifter function of 3. what is your guess:")
    if guess==s2:
        print("yay! you may pass")
        return
    return

			
#a function that adds fruit into random places around the left half of  map		
def add_fruit():
    #to place the appples randomly
    random_y_apple= random.randint(5,len(Map)-3)
    random_x_apple= random.randint(1,5)
    Map[random_y_apple][random_x_apple]=5


#a function that adds planks into random places around the left half of map    
def add_planks():
    # to place the planks randomly
    random_y_plank= random.randint(5,len(Map)-3)
    random_x_plank= random.randint(1,5)
    Map[random_y_plank][random_x_plank]=2
    
    
#to check if the player collected apples
def check_collisions(x,y):
    global inventory
    if Map[y][x]==APPLE: #if square player is on, is an apple, it will add one to their inventory
        Map[y][x]=0
        inventory[0][1]=inventory[0][1]+1
        add_fruit()
        

#print the players inventory before each turn
def print_inventory():
    t.clear() #clear the screen so you can actually read what it says
    t.penup()
    t.goto(LEFT_EDGE,TOP_EDGE)
    for x in range(0,len(inventory)):
        #print("you have", inventory[x][1],inventory[x][0])
        t.pendown()
        t.write((inventory[x][0]+": ",inventory[x][1]), font=("Comic Sans", 25,"normal"))
        t.penup()
        t.goto(0,TOP_EDGE)
        t.penup()
        

#place power up in specific spot with 50% chance of spawning
def place_power_up():
    powerUp=random.randint(0,10)
    if powerUp<5:  #if the chance is less than 50, power up will not spawn
        Map[4][2]=0
    return

#functions that checks first if you have the power up, then executes its purpose for 5 moves
def power_up(x,y):
    global powerUpTurn,power

    if Map[y][x]==POWERUP:  #If you are on the powerup
        powerUp=eventList[Map[y][x]][3]
        turtle.textinput("Power Up", powerUp)
        Map[y][x]=0
        eventList[PLANK][2]="black" #the planks will appear as a black square
        power=True
        
    if power==True:
        turnsleft=powerUpTurn
        #turtle.textinput("Power Up Moves Left:",powerUpTurn) #I decided not to add this either because it would pop up before you character moved, and it was kind of annoying
        print("you have",powerUpTurn,"moves left for your power up.") #each turn it will print how many moves you have before power up goes away
        powerUpTurn=powerUpTurn-1
        if powerUpTurn<0: #once there are no  more turns left, the planks are invisible again
            power=False   #so that they can no longer see the planks
            eventList[PLANK][2]="peru" #they go back to being the same color as the 
        return
    return

#function to move player right
def movePlayerR():
    global currX,currY
    if Map[currY][currX+1] != 1:
        power_up(currX,currY) #to check if they got the power up (it won't work if you just put it in the check collisions or check event function)
        player.seth(0) #right
        player.forward(sidelen) #moves right the width of each box
        currX=currX+1
    return

#function to move player left
def movePlayerL():
    global currX,currY
    if Map[currY][currX-1] != 1:
        power_up(currX,currY)  #to check if they got the power up
        player.seth(180) #left
        player.forward(sidelen) #moves left the width of each box
        currX=currX-1 
    return

#function to move player up
def movePlayerU():
    global currX,currY
    if Map[currY-1][currX] != 1:
        power_up(currX,currY) #to check if they got the power up
        player.seth(90) #up
        player.forward(sideheight) #moves up the length of each box
        currY=currY-1
    return

#function to move player down
def movePlayerD():
    global currX,currY
    if Map[currY+1][currX] != 1:
        power_up(currX,currY) #to check if they got the power up
        player.seth(270) #down
        player.forward(sideheight) #moves down the length of each box
        currY=currY+1
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
for fruit in range(0,4): #puts four random apples, that respawn
    add_fruit()
    
for planks in range(0,4): #puts four random planks
    add_planks()

    
#draw the map the first time before asking for a move
#drawMap(currX, currY)
screen.tracer(0) #screen tracer off so we dont have to see everything being drawn

#tell player to put in full screen because they can play the whole game on the graphics screen after their read the instructions
turtle.textinput("Put game in full screen for best results", "")

##ball.goto(LEFT_EDGE-currX*(0-sidelen)+(sidelen/2),currY*sideheight-(sideheight/2))

#key comands for game
turtle.onkey(movePlayerD,"Down") #key command for down arrow
turtle.onkey(movePlayerU,"Up")   #key command for up arrow
turtle.onkey(movePlayerL,"Left") #key command for left arrow
turtle.onkey(movePlayerR,"Right")#key command for right arrow

#player#
player=Turtle()
player.shape("square")
player.color("white")
player.penup()
player.shapesize(stretch_wid=sidelen/20-1, stretch_len=sideheight/20-1) #to fit the size of the squares on my specific map


#Let the player move around the map on the path until they reach the end of the game
while gamePlay==True: #if they say yes to playing the game
    turtle.listen()
    draw_turtle_map() #draw the actual map
    player.goto(((LEFT_EDGE+sidelen*currX)+sidelen/2),(TOP_EDGE-sideheight*(currY+1)+(sideheight/2))) #moves the player based on the currX and currY
    check_Event(currX,currY)  #checks if they are in an event square
    check_collisions(currX,currY) #checks if they collided w anything
    screen.update()
    
    print_inventory() #prints their inventory

screen.clear()
turtle.penup()
turtle.goto(-125,0)
turtle.write("YOU WIN!!",font=("Times New Roman",50))
